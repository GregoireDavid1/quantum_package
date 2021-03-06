===========
Dets Module
===========

This module contains the determinants of the CI wave function.

H is applied on the list of generator determinants. Selected determinants
are added into the *H_apply buffer*. Then the new wave function is
constructred as the concatenation of the odl wave function and
some determinants of the H_apply buffer. Generator determinants are built
as a subset of the determinants of the wave function.


Assumptions
===========

.. Do not edit this section. It was auto-generated from the
.. NEEDED_MODULES file.

* The MOs are orthonormal
* All the determinants have the same number of electrons
* The determinants are orthonormal
* The number of generator determinants <= the number of determinants
* All the determinants in the H_apply buffer are supposed to be different from the 
  wave function determinants
* All the determinants in the H_apply buffer are supposed to be unique


Needed Modules
==============

.. Do not edit this section. It was auto-generated from the
.. NEEDED_MODULES file.

.. image:: tree_dependancy.png

* `Integrals_Monoelec <http://github.com/LCPQ/quantum_package/tree/master/src/Integrals_Monoelec>`_
* `Integrals_Bielec <http://github.com/LCPQ/quantum_package/tree/master/src/Integrals_Bielec>`_

Documentation
=============

.. Do not edit this section. It was auto-generated from the
.. NEEDED_MODULES file.

`copy_h_apply_buffer_to_wf <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/H_apply.irp.f#L103>`_
  Copies the H_apply buffer to psi_coef.
  After calling this subroutine, N_det, psi_det and psi_coef need to be touched

`fill_h_apply_buffer_no_selection <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/H_apply.irp.f#L258>`_
  Fill the H_apply buffer with determiants for CISD

`h_apply_buffer_allocated <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/H_apply.irp.f#L15>`_
  Buffer of determinants/coefficients/perturbative energy for H_apply.
  Uninitialized. Filled by H_apply subroutines.

`h_apply_buffer_lock <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/H_apply.irp.f#L16>`_
  Buffer of determinants/coefficients/perturbative energy for H_apply.
  Uninitialized. Filled by H_apply subroutines.

`remove_duplicates_in_psi_det <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/H_apply.irp.f#L190>`_
  Removes duplicate determinants in the wave function.

`resize_h_apply_buffer <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/H_apply.irp.f#L48>`_
  Resizes the H_apply buffer of proc iproc. The buffer lock should
  be set before calling this function.

`cisd_sc2 <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/SC2.irp.f#L1>`_
  CISD+SC2 method              :: take off all the disconnected terms of a CISD (selected or not)
  .br
  dets_in : bitmasks corresponding to determinants
  .br
  u_in : guess coefficients on the various states. Overwritten
  on exit
  .br
  dim_in : leftmost dimension of u_in
  .br
  sze : Number of determinants
  .br
  N_st : Number of eigenstates
  .br
  Initial guess vectors are not necessarily orthonormal

`connected_to_ref <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/connected_to_ref.irp.f#L155>`_
  Undocumented

`connected_to_ref_by_mono <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/connected_to_ref.irp.f#L253>`_
  Undocumented

`det_search_key <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/connected_to_ref.irp.f#L1>`_
  Return an integer*8 corresponding to a determinant index for searching

`get_index_in_psi_det_sorted_bit <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/connected_to_ref.irp.f#L48>`_
  Returns the index of the determinant in the ``psi_det_sorted_bit`` array

`is_in_wavefunction <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/connected_to_ref.irp.f#L34>`_
  True if the determinant ``det`` is in the wave function

`occ_pattern_search_key <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/connected_to_ref.irp.f#L17>`_
  Return an integer*8 corresponding to a determinant index for searching

`do_mono_excitation <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/create_excitations.irp.f#L1>`_
  Apply the mono excitation operator : a^{dager}_(i_particle) a_(i_hole) of spin = ispin
  on key_in
  ispin = 1  == alpha
  ispin = 2  == beta
  i_ok = 1  == the excitation is possible
  i_ok = -1 == the excitation is not possible

`davidson_converged <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/davidson.irp.f#L382>`_
  True if the Davidson algorithm is converged

`davidson_criterion <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/davidson.irp.f#L372>`_
  Can be : [  energy  | residual | both | wall_time | cpu_time | iterations ]

`davidson_diag <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/davidson.irp.f#L18>`_
  Davidson diagonalization.
  .br
  dets_in : bitmasks corresponding to determinants
  .br
  u_in : guess coefficients on the various states. Overwritten
  on exit
  .br
  dim_in : leftmost dimension of u_in
  .br
  sze : Number of determinants
  .br
  N_st : Number of eigenstates
  .br
  iunit : Unit number for the I/O
  .br
  Initial guess vectors are not necessarily orthonormal

`davidson_diag_hjj <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/davidson.irp.f#L68>`_
  Davidson diagonalization with specific diagonal elements of the H matrix
  .br
  H_jj : specific diagonal H matrix elements to diagonalize de Davidson
  .br
  dets_in : bitmasks corresponding to determinants
  .br
  u_in : guess coefficients on the various states. Overwritten
  on exit
  .br
  dim_in : leftmost dimension of u_in
  .br
  sze : Number of determinants
  .br
  N_st : Number of eigenstates
  .br
  iunit : Unit for the I/O
  .br
  Initial guess vectors are not necessarily orthonormal

`davidson_iter_max <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/davidson.irp.f#L1>`_
  Max number of Davidson iterations

`davidson_sze_max <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/davidson.irp.f#L9>`_
  Max number of Davidson sizes

`davidson_threshold <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/davidson.irp.f#L373>`_
  Can be : [  energy  | residual | both | wall_time | cpu_time | iterations ]

`one_body_dm_mo <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/density_matrix.irp.f#L164>`_
  One-body density matrix

`one_body_dm_mo_alpha <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/density_matrix.irp.f#L1>`_
  Alpha and beta one-body density matrix for each state

`one_body_dm_mo_beta <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/density_matrix.irp.f#L2>`_
  Alpha and beta one-body density matrix for each state

`one_body_single_double_dm_mo_alpha <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/density_matrix.irp.f#L80>`_
  Alpha and beta one-body density matrix for each state

`one_body_single_double_dm_mo_beta <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/density_matrix.irp.f#L81>`_
  Alpha and beta one-body density matrix for each state

`one_body_spin_density_mo <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/density_matrix.irp.f#L172>`_
  rho(alpha) - rho(beta)

`save_natural_mos <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/density_matrix.irp.f#L196>`_
  Save natural orbitals, obtained by diagonalization of the one-body density matrix in the MO basis

`set_natural_mos <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/density_matrix.irp.f#L180>`_
  Set natural orbitals, obtained by diagonalization of the one-body density matrix in the MO basis

`state_average_weight <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/density_matrix.irp.f#L207>`_
  Weights in the state-average calculation of the density matrix

`det_svd <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/det_svd.irp.f#L1>`_
  Computes the SVD of the Alpha x Beta determinant coefficient matrix

`filter_3_highest_electrons <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L423>`_
  Returns a determinant with only the 3 highest electrons

`int_of_3_highest_electrons <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L388>`_
  Returns an integer*8 as :
  .br
  |_<--- 21 bits ---><--- 21 bits ---><--- 21 bits --->|
  .br
  |0<---   i1    ---><---   i2    ---><---   i3    --->|
  .br
  It encodes the value of the indices of the 3 highest MOs
  in descending order
  .br

`max_degree_exc <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L32>`_
  Maximum degree of excitation in the wf

`n_det <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L3>`_
  Number of determinants in the wave function

`psi_average_norm_contrib <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L273>`_
  Contribution of determinants to the state-averaged density

`psi_average_norm_contrib_sorted <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L303>`_
  Wave function sorted by determinants contribution to the norm (state-averaged)

`psi_coef <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L227>`_
  The wave function coefficients. Initialized with Hartree-Fock if the EZFIO file
  is empty

`psi_coef_sorted <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L302>`_
  Wave function sorted by determinants contribution to the norm (state-averaged)

`psi_coef_sorted_ab <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L450>`_
  Determinants on which we apply <i|H|j>.
  They are sorted by the 3 highest electrons in the alpha part,
  then by the 3 highest electrons in the beta part to accelerate
  the research of connected determinants.

`psi_coef_sorted_bit <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L333>`_
  Determinants on which we apply <i|H|psi> for perturbation.
  They are sorted by determinants interpreted as integers. Useful
  to accelerate the search of a random determinant in the wave
  function.

`psi_det <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L65>`_
  The wave function determinants. Initialized with Hartree-Fock if the EZFIO file
  is empty

`psi_det_size <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L47>`_
  Size of the psi_det/psi_coef arrays

`psi_det_sorted <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L301>`_
  Wave function sorted by determinants contribution to the norm (state-averaged)

`psi_det_sorted_ab <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L449>`_
  Determinants on which we apply <i|H|j>.
  They are sorted by the 3 highest electrons in the alpha part,
  then by the 3 highest electrons in the beta part to accelerate
  the research of connected determinants.

`psi_det_sorted_bit <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L332>`_
  Determinants on which we apply <i|H|psi> for perturbation.
  They are sorted by determinants interpreted as integers. Useful
  to accelerate the search of a random determinant in the wave
  function.

`psi_det_sorted_next_ab <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L451>`_
  Determinants on which we apply <i|H|j>.
  They are sorted by the 3 highest electrons in the alpha part,
  then by the 3 highest electrons in the beta part to accelerate
  the research of connected determinants.

`read_dets <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L580>`_
  Reads the determinants from the EZFIO file

`save_wavefunction <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L627>`_
  Save the wave function into the EZFIO file

`save_wavefunction_general <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L646>`_
  Save the wave function into the EZFIO file

`save_wavefunction_unsorted <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L637>`_
  Save the wave function into the EZFIO file

`sort_dets_by_3_highest_electrons <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L471>`_
  Determinants on which we apply <i|H|j>.
  They are sorted by the 3 highest electrons in the alpha part,
  then by the 3 highest electrons in the beta part to accelerate
  the research of connected determinants.

`sort_dets_by_det_search_key <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants.irp.f#L346>`_
  Determinants are sorted are sorted according to their det_search_key.
  Useful to accelerate the search of a random determinant in the wave
  function.

`double_exc_bitmask <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants_bitmasks.irp.f#L40>`_
  double_exc_bitmask(:,1,i) is the bitmask for holes of excitation 1
  double_exc_bitmask(:,2,i) is the bitmask for particles of excitation 1
  double_exc_bitmask(:,3,i) is the bitmask for holes of excitation 2
  double_exc_bitmask(:,4,i) is the bitmask for particles of excitation 2
  for a given couple of hole/particle excitations i.

`n_double_exc_bitmasks <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants_bitmasks.irp.f#L31>`_
  Number of double excitation bitmasks

`n_single_exc_bitmasks <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants_bitmasks.irp.f#L8>`_
  Number of single excitation bitmasks

`single_exc_bitmask <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/determinants_bitmasks.irp.f#L17>`_
  single_exc_bitmask(:,1,i) is the bitmask for holes
  single_exc_bitmask(:,2,i) is the bitmask for particles
  for a given couple of hole/particle excitations i.

`ci_eigenvectors <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI.irp.f#L37>`_
  Eigenvectors/values of the CI matrix

`ci_eigenvectors_s2 <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI.irp.f#L38>`_
  Eigenvectors/values of the CI matrix

`ci_electronic_energy <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI.irp.f#L36>`_
  Eigenvectors/values of the CI matrix

`ci_energy <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI.irp.f#L18>`_
  N_states lowest eigenvalues of the CI matrix

`diag_algorithm <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI.irp.f#L1>`_
  Diagonalization algorithm (Davidson or Lapack)

`diagonalize_ci <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI.irp.f#L100>`_
  Replace the coefficients of the CI states by the coefficients of the
  eigenstates of the CI matrix

`ci_sc2_eigenvectors <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI_SC2.irp.f#L27>`_
  Eigenvectors/values of the CI matrix

`ci_sc2_electronic_energy <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI_SC2.irp.f#L26>`_
  Eigenvectors/values of the CI matrix

`ci_sc2_energy <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI_SC2.irp.f#L1>`_
  N_states_diag lowest eigenvalues of the CI matrix

`diagonalize_ci_sc2 <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI_SC2.irp.f#L45>`_
  Replace the coefficients of the CI states_diag by the coefficients of the
  eigenstates of the CI matrix

`threshold_convergence_sc2 <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI_SC2.irp.f#L18>`_
  convergence of the correlation energy of SC2 iterations

`ci_eigenvectors_mono <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI_mono.irp.f#L2>`_
  Eigenvectors/values of the CI matrix

`ci_eigenvectors_s2_mono <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI_mono.irp.f#L3>`_
  Eigenvectors/values of the CI matrix

`ci_electronic_energy_mono <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI_mono.irp.f#L1>`_
  Eigenvectors/values of the CI matrix

`diagonalize_ci_mono <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/diagonalize_CI_mono.irp.f#L73>`_
  Replace the coefficients of the CI states by the coefficients of the
  eigenstates of the CI matrix

`apply_mono <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/excitations_utils.irp.f#L1>`_
  Undocumented

`filter_connected <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/filter_connected.irp.f#L2>`_
  Filters out the determinants that are not connected by H
  .br
  returns the array idx which contains the index of the
  .br
  determinants in the array key1 that interact
  .br
  via the H operator with key2.
  .br
  idx(0) is the number of determinants that interact with key1

`filter_connected_davidson <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/filter_connected.irp.f#L163>`_
  Filters out the determinants that are not connected by H
  returns the array idx which contains the index of the
  determinants in the array key1 that interact
  via the H operator with key2.
  .br
  idx(0) is the number of determinants that interact with key1
  key1 should come from psi_det_sorted_ab.

`filter_connected_i_h_psi0 <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/filter_connected.irp.f#L293>`_
  returns the array idx which contains the index of the
  .br
  determinants in the array key1 that interact
  .br
  via the H operator with key2.
  .br
  idx(0) is the number of determinants that interact with key1

`filter_connected_i_h_psi0_sc2 <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/filter_connected.irp.f#L392>`_
  standard filter_connected_i_H_psi but returns in addition
  .br
  the array of the index of the non connected determinants to key1
  .br
  in order to know what double excitation can be repeated on key1
  .br
  idx_repeat(0) is the number of determinants that can be used
  .br
  to repeat the excitations

`filter_connected_sorted_ab <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/filter_connected.irp.f#L101>`_
  Filters out the determinants that are not connected by H
  returns the array idx which contains the index of the
  determinants in the array key1 that interact
  via the H operator with key2.
  idx(0) is the number of determinants that interact with key1
  .br
  Determinants are taken from the psi_det_sorted_ab array

`put_gess <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/guess_triplet.irp.f#L1>`_
  Undocumented

`det_to_occ_pattern <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/occ_pattern.irp.f#L2>`_
  Transform a determinant to an occupation pattern

`make_s2_eigenfunction <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/occ_pattern.irp.f#L251>`_
  Undocumented

`n_occ_pattern <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/occ_pattern.irp.f#L143>`_
  array of the occ_pattern present in the wf
  psi_occ_pattern(:,1,j) = jth occ_pattern of the wave function : represent all the single occupation
  psi_occ_pattern(:,2,j) = jth occ_pattern of the wave function : represent all the double occupation

`occ_pattern_to_dets <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/occ_pattern.irp.f#L42>`_
  Generate all possible determinants for a give occ_pattern

`occ_pattern_to_dets_size <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/occ_pattern.irp.f#L20>`_
  Number of possible determinants for a given occ_pattern

`psi_occ_pattern <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/occ_pattern.irp.f#L142>`_
  array of the occ_pattern present in the wf
  psi_occ_pattern(:,1,j) = jth occ_pattern of the wave function : represent all the single occupation
  psi_occ_pattern(:,2,j) = jth occ_pattern of the wave function : represent all the double occupation

`rec_occ_pattern_to_dets <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/occ_pattern.irp.f#L102>`_
  Undocumented

`n_states_diag <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/options.irp.f#L1>`_
  Number of states to consider for the diagonalization

`pouet <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/program_beginer_determinants.irp.f#L1>`_
  Undocumented

`routine <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/program_beginer_determinants.irp.f#L7>`_
  Undocumented

`idx_cas <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/psi_cas.irp.f#L5>`_
  CAS wave function, defined from the application of the CAS bitmask on the
  determinants. idx_cas gives the indice of the CAS determinant in psi_det.

`idx_non_cas <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/psi_cas.irp.f#L62>`_
  Set of determinants which are not part of the CAS, defined from the application
  of the CAS bitmask on the determinants.
  idx_non_cas gives the indice of the determinant in psi_det.

`n_det_cas <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/psi_cas.irp.f#L6>`_
  CAS wave function, defined from the application of the CAS bitmask on the
  determinants. idx_cas gives the indice of the CAS determinant in psi_det.

`n_det_non_cas <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/psi_cas.irp.f#L63>`_
  Set of determinants which are not part of the CAS, defined from the application
  of the CAS bitmask on the determinants.
  idx_non_cas gives the indice of the determinant in psi_det.

`psi_cas <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/psi_cas.irp.f#L3>`_
  CAS wave function, defined from the application of the CAS bitmask on the
  determinants. idx_cas gives the indice of the CAS determinant in psi_det.

`psi_cas_coef <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/psi_cas.irp.f#L4>`_
  CAS wave function, defined from the application of the CAS bitmask on the
  determinants. idx_cas gives the indice of the CAS determinant in psi_det.

`psi_cas_coef_sorted_bit <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/psi_cas.irp.f#L47>`_
  CAS determinants sorted to accelerate the search of a random determinant in the wave
  function.

`psi_cas_sorted_bit <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/psi_cas.irp.f#L46>`_
  CAS determinants sorted to accelerate the search of a random determinant in the wave
  function.

`psi_non_cas <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/psi_cas.irp.f#L60>`_
  Set of determinants which are not part of the CAS, defined from the application
  of the CAS bitmask on the determinants.
  idx_non_cas gives the indice of the determinant in psi_det.

`psi_non_cas_coef <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/psi_cas.irp.f#L61>`_
  Set of determinants which are not part of the CAS, defined from the application
  of the CAS bitmask on the determinants.
  idx_non_cas gives the indice of the determinant in psi_det.

`psi_non_cas_coef_sorted_bit <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/psi_cas.irp.f#L100>`_
  CAS determinants sorted to accelerate the search of a random determinant in the wave
  function.

`psi_non_cas_sorted_bit <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/psi_cas.irp.f#L99>`_
  CAS determinants sorted to accelerate the search of a random determinant in the wave
  function.

`bi_elec_ref_bitmask_energy <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/ref_bitmask.irp.f#L5>`_
  Energy of the reference bitmask used in Slater rules

`kinetic_ref_bitmask_energy <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/ref_bitmask.irp.f#L3>`_
  Energy of the reference bitmask used in Slater rules

`mono_elec_ref_bitmask_energy <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/ref_bitmask.irp.f#L2>`_
  Energy of the reference bitmask used in Slater rules

`nucl_elec_ref_bitmask_energy <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/ref_bitmask.irp.f#L4>`_
  Energy of the reference bitmask used in Slater rules

`ref_bitmask_energy <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/ref_bitmask.irp.f#L1>`_
  Energy of the reference bitmask used in Slater rules

`expected_s2 <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/s2.irp.f#L48>`_
  Expected value of S2 : S*(S+1)

`get_s2 <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/s2.irp.f#L1>`_
  Returns <S^2>

`get_s2_u0 <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/s2.irp.f#L82>`_
  Undocumented

`s2_values <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/s2.irp.f#L67>`_
  array of the averaged values of the S^2 operator on the various states

`s_z <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/s2.irp.f#L36>`_
  z component of the Spin

`s_z2_sz <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/s2.irp.f#L37>`_
  z component of the Spin

`prog_save_casino <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/save_for_casino.irp.f#L266>`_
  Undocumented

`save_casino <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/save_for_casino.irp.f#L1>`_
  Undocumented

`save_natorb <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/save_natorb.irp.f#L1>`_
  Undocumented

`a_operator <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L962>`_
  Needed for diag_H_mat_elem

`ac_operator <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L1007>`_
  Needed for diag_H_mat_elem

`decode_exc <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L76>`_
  Decodes the exc arrays returned by get_excitation.
  h1,h2 : Holes
  p1,p2 : Particles
  s1,s2 : Spins (1:alpha, 2:beta)
  degree : Degree of excitation

`det_connections <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L1139>`_
  Build connection proxy between determinants

`diag_h_mat_elem <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L900>`_
  Computes <i|H|i>

`get_double_excitation <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L141>`_
  Returns the two excitation operators between two doubly excited determinants and the phase

`get_excitation <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L30>`_
  Returns the excitation operators between two determinants and the phase

`get_excitation_degree <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L1>`_
  Returns the excitation degree between two determinants

`get_excitation_degree_vector <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L816>`_
  Applies get_excitation_degree to an array of determinants

`get_mono_excitation <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L274>`_
  Returns the excitation operator between two singly excited determinants and the phase

`get_occ_from_key <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L1055>`_
  Returns a list of occupation numbers from a bitstring

`h_u_0 <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L1071>`_
  Computes v_0 = H|u_0>
  .br
  n : number of determinants
  .br
  H_jj : array of <j|H|j>

`i_h_j <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L355>`_
  Returns <i|H|j> where i and j are determinants

`i_h_j_verbose <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L492>`_
  Returns <i|H|j> where i and j are determinants

`i_h_psi <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L631>`_
  <key|H|psi> for the various Nstates

`i_h_psi_sc2 <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L713>`_
  <key|H|psi> for the various Nstate
  .br
  returns in addition
  .br
  the array of the index of the non connected determinants to key1
  .br
  in order to know what double excitation can be repeated on key1
  .br
  idx_repeat(0) is the number of determinants that can be used
  .br
  to repeat the excitations

`i_h_psi_sc2_verbose <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L760>`_
  <key|H|psi> for the various Nstate
  .br
  returns in addition
  .br
  the array of the index of the non connected determinants to key1
  .br
  in order to know what double excitation can be repeated on key1
  .br
  idx_repeat(0) is the number of determinants that can be used
  .br
  to repeat the excitations

`i_h_psi_sec_ord <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L666>`_
  <key|H|psi> for the various Nstates

`n_con_int <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/slater_rules.irp.f#L1131>`_
  Number of integers to represent the connections between determinants

`create_wf_of_psi_svd_matrix <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L483>`_
  Matrix of wf coefficients. Outer product of alpha and beta determinants

`generate_all_alpha_beta_det_products <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L538>`_
  Create a wave function from all possible alpha x beta determinants

`get_index_in_psi_det_alpha_unique <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L139>`_
  Returns the index of the determinant in the ``psi_det_alpha_unique`` array

`get_index_in_psi_det_beta_unique <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L221>`_
  Returns the index of the determinant in the ``psi_det_beta_unique`` array

`psi_det_alpha <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L25>`_
  List of alpha determinants of psi_det

`psi_det_beta <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L39>`_
  List of beta determinants of psi_det

`psi_svd_alpha <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L578>`_
  SVD wave function

`psi_svd_beta <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L579>`_
  SVD wave function

`psi_svd_coefs <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L580>`_
  SVD wave function

`psi_svd_matrix <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L467>`_
  Matrix of wf coefficients. Outer product of alpha and beta determinants

`psi_svd_matrix_columns <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L407>`_
  Matrix of wf coefficients. Outer product of alpha and beta determinants

`psi_svd_matrix_rows <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L406>`_
  Matrix of wf coefficients. Outer product of alpha and beta determinants

`psi_svd_matrix_values <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L405>`_
  Matrix of wf coefficients. Outer product of alpha and beta determinants

`spin_det_search_key <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L9>`_
  Return an integer*8 corresponding to a determinant index for searching

`write_spindeterminants <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/spindeterminants.irp.f#L303>`_
  Undocumented

`cisd <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/truncate_wf.irp.f#L1>`_
  Undocumented

`h_matrix_all_dets <http://github.com/LCPQ/quantum_package/tree/master/src/Determinants/utils.irp.f#L1>`_
  H matrix on the basis of the slater determinants defined by psi_det



