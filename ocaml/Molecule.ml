open Core.Std ;;
open Qptypes ;;

exception MultiplicityError of string;;

type t = {
  nuclei     : Atom.t list ;
  elec_alpha : Elec_alpha_number.t ;
  elec_beta  : Elec_beta_number.t ;
} with sexp

let get_charge { nuclei  ; elec_alpha ; elec_beta } =
  let result = (Elec_alpha_number.to_int elec_alpha) +
     (Elec_beta_number.to_int elec_beta) in
  let rec nucl_charge = function
  | a::rest -> (Charge.to_float a.Atom.charge) +. nucl_charge rest
  | [] -> 0.
  in
  Charge.of_float (nucl_charge nuclei  -. (Float.of_int result))
;;

let get_multiplicity m = 
  let elec_alpha = m.elec_alpha in
  Multiplicity.of_alpha_beta elec_alpha m.elec_beta
;;

let get_nucl_num m =
  let nmax = (List.length m.nuclei) in
  Nucl_number.of_int nmax ~max:nmax
;;

let name m = 
  let cm = Charge.to_int (get_charge m) in
  let c = 
     match cm with
     | 0 -> ""
     | 1 -> " (+)"
     | (-1) -> " (-)"
     | i when i>1 -> Printf.sprintf " (%d+)" i
     | i -> Printf.sprintf " (%d-)" (-i)
  in
  let mult = Multiplicity.to_string (get_multiplicity m) in
  let { nuclei  ; elec_alpha ; elec_beta } = m in
  let rec build_list accu = function
  | a::rest ->
      begin
        let e = a.Atom.element in
        match (List.Assoc.find accu e) with
        | None   -> build_list (List.Assoc.add accu e 1) rest
        | Some i -> build_list (List.Assoc.add accu e (i+1)) rest
      end
  | [] -> accu
  in
  let rec build_name accu = function
  | (a, n)::rest ->
    let a = Element.to_string a in
    begin
      match n with 
      | 1 -> build_name (a::accu) rest
      | i when i>1 -> 
        let tmp = Printf.sprintf "%s%d" a i
        in build_name (tmp::accu) rest
      | _ -> assert false
    end
  | [] -> accu
  in
  let result = build_list [] nuclei |> build_name [c ; ", " ; mult]
  in
  String.concat (result)
;;

let to_string m =
  let { nuclei  ; elec_alpha ; elec_beta } = m in
  let n = List.length nuclei in
  let title = name m in
  [ Int.to_string n ; title ] @ (List.map ~f:(fun x -> Atom.to_string
  Units.Angstrom x) nuclei)
  |> String.concat ~sep:"\n"
;;

let of_xyz_string
    ?(charge=(Charge.of_int 0)) ?(multiplicity=(Multiplicity.of_int 1))
    ?(units=Units.Angstrom)
    s =
  let l = String.split s ~on:'\n'
       |> List.filter ~f:(fun x -> x <> "")
       |> List.map ~f:(fun x -> Atom.of_string units x)
  in
  let ne = ( get_charge { 
        nuclei=l ;
        elec_alpha=(Elec_alpha_number.of_int 1) ;
        elec_beta=(Elec_beta_number.of_int 0) } 
      |> Charge.to_int 
      ) + 1 - (Charge.to_int charge)
      |> Elec_number.of_int 
  in
  let (na,nb) = Multiplicity.to_alpha_beta ne multiplicity in
  let result = 
  { nuclei = l ;
    elec_alpha = na ;
    elec_beta  = nb }
  in
  if ((get_multiplicity result) <> multiplicity) then
     let msg = Printf.sprintf
      "With %d electrons multiplicity %d is impossible"
      (Elec_number.to_int ne)
      (Multiplicity.to_int multiplicity)
     in
     raise (MultiplicityError msg);
  else () ;
  result
;;


let of_xyz_file
    ?(charge=(Charge.of_int 0)) ?(multiplicity=(Multiplicity.of_int 1))
    ?(units=Units.Angstrom)
    filename =
  let (_,buffer) = In_channel.read_all filename 
  |> String.lsplit2_exn ~on:'\n' in
  let (_,buffer) = String.lsplit2_exn buffer ~on:'\n' in
  of_xyz_string ~charge:charge ~multiplicity:multiplicity 
    ~units:units buffer
;;

include To_md5;;
let to_md5 = to_md5 sexp_of_t
;;
