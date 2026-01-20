import streamlit as st


# Sugarcane Disease and Pest Management Expert System


class SugarcaneExpertSystem:
    def __init__(self):
        # Define all diseases to act as the domain knowledge
        self.diseases = [
            'red_rot', 'smut', 'wilt', 'sett_rot', 'ratoon_stunting_disease',
            'grassy_shoot', 'mosaic', 'yellow_leaf_disease', 'pokkah_boeng',
            'leaf_fleck', 'rust', 'eye_spot', 'brown_spot', 'yellow_spot',
            'brown_stripe', 'ring_spot', 'leaf_scald', 'leaf_blast',
            'curvularia_leaf_spot', 'orange_rust'
        ]

        # Define all symptoms
        self.symptoms = [
            'reddened_areas_with_white_patches', 'affected_parenchymatous_tissues',
            'hollow_cavity_with_grey_mycelium', 'dark_brownish_lesions_on_rind',
            'necrosis_on_nodal_region', 'cut_ends_show_reddening', 'entire_stool_dries',
            'excessive_tillering_lanky', 'black_whip_structures', 'whip_like_sorus_bearing_structures',
            'stunted_thin_canes', 'narrow_weak_leaves', 'proliferating_axillary_buds',
            'stem_or_leaf_galls', 'yellowish_stools_drying', 'dull_brownish_discolouration_internal',
            'linear_pith_cavities', 'dried_canes_detopped_crown', 'yellowish_foliage',
            'pineapple_odor', 'setts_fail_to_germinate', 'sett_rot_before_germination',
            'shoot_die_after_emergence', 'stunted_chlorotic_shoots', 'sett_blackening_with_spores',
            'wilting_and_withering', 'stunted_growth', 'reduced_tillering', 'thin_stalks_shortened_internodes',
            'vascular_bundle_discolouration_nodes', 'narrow_leaves', 'grass_like_appearance',
            'chlorotic_areas_young_leaves', 'yellowish_stripes', 'mild_mottling', 'yellowing',
            'necrosis', 'yellowish_midrib_lower_surface', 'reddish_pinkish_discolouration_midrib',
            'shortening_internodes_top', 'bunching_leaves_top', 'reduced_cane_thickness',
            'malformed_twisted_top', 'white_mycelium_on_leaves', 'wrinkling_twisting_shortening_leaves',
            'irregular_reddish_stripes_specks', 'knife_cut_symptoms', 'top_rot',
            'flecks_specks_leaf_lamina', 'premature_leaf_drying', 'tiny_chlorotic_flecks',
            'mottling_on_middle_leaves', 'reddening_and_drying', 'fleck_coalescence',
            'reduced_plant_vigor', 'rust_pustules', 'small_chlorotic_puncta',
            'brown_tawny_pustules', 'lesion_coalescence', 'reduced_canopy_density',
            'orange_powdery_pustules', 'yellow_orange_streaks_on_leaves', 'pustules_between_leaf_veins',
            'leaf_yellowing', 'eye_shaped_spots', 'minute_water_soaked_spots_on_young_leaves',
            'reddish_brown_elliptical_lesions_parallel_to_veins',
            'lesions_0_5_to_4_mm_long_with_yellowish_brown_margins', 'grey_or_tan_center_in_mature_spots',
            'reddish_brown_to_yellowish_runners_streaking_toward_leaf_tip',
            'lesions_may_coalesce_into_long_streaks', 'seedling_blight_and_top_rot_in_severe_infections',
            'red_brown_oval_or_elliptical_lesions_on_leaf_blade', 'lesion_size_approximately_3_to_15_mm',
            'narrow_yellow_halo_around_spots', 'spots_may_increase_and_coalesce_forming_larger_necrotic_areas',
            'occurs_from_seedling_stage_through_maturity_under_favourable_conditions',
            'yellow_spots', 'brown_spots', 'small_yellow_leaf_lesions_initially',
            'lesions_enlarge_and_turn_reddish_or_brown_with_age',
            'splotchy_yellow_lesions_that_may_transition_to_brown',
            'gray_fuzzy_down_of_conidiophores_often_on_leaf_underside',
            'visible_from_distance_when_widespread_in_canopy_wet_tropics',
            'brown_stripes', 'brown_lesions_along_leaf_blades_parallel_to_veins',
            'narrow_dark_brown_stripes_on_young_leaves',
            'lesions_may_merge_into_bands_covering_large_leaf_area',
            'disease_develops_under_warm_humid_conditions', 'ring_shaped_spots',
            'small_elongated_or_oval_spots_dark_olivaceous_green_to_reddish_brown',
            'narrow_yellow_halo_surrounding_each_spot',
            'larger_elongated_lesions_2_5_to_5_mm_x_10_to_18_mm_with_red_brown_margins',
            'spots_coalesce_into_patches_leading_to_leaf_chlorosis_and_necrosis',
            'small_black_fruiting_bodies_may_be_visible_in_old_lesions',
            'yellow_narrow_spots_with_long_axes_parallel_to_vessels',
            'small_yellowish_or_pale_spots_on_leaf_blades_initially',
            'spots_extend_long_axes_parallel_to_leaf_veins',
            'lesions_turn_brown_and_merge_into_larger_blighted_areas',
            'severe_infection_causes_whole_leaf_to_wither_and_dry',
            'slight_pale_yellow_ribbon_on_first_five_leaves', 'red_changes_around_lesion',
            'small_to_medium_brown_or_reddish_elliptical_lesions_on_leaves',
            'pale_yellow_ribbon_or_band_on_first_few_leaves_of_seedlings',
            'red_or_reddish_margin_or_red_changes_around_lesion_center',
            'lesions_may_coalesce_and_cause_early_leaf_senescence',
            'white_stripes_on_leaves', 'leaf_yellowing_from_tip', 'cane_death_in_advanced_infection',
            'leaf_rust_brown_patches', 'wilting_of_whole_plant'
        ]

        # Define all pests
        self.pests = [
            'colletotrichum_falcatum', 'sporisorium_scitamineum', 'fusarium_sacchari',
            'ceratocystis_paradoxa', 'leifsonia_xyli', 'sugarcane_grassy_shoot_phytoplasma',
            'sugarcane_mosaic_virus', 'sugarcane_yellow_leaf_virus', 'fusarium_verticillioides',
            'fusarium_proliferatum', 'sugarcane_bacilliform_virus', 'foliar_fungus',
            'xanthomonas_albilineans', 'white_grub', 'root_borer', 'stem_borer',
            'nematode', 'mealy_bug', 'scale_insect', 'oligonychus_stickneyi',
            'oligonychus_pratensis', 'oligonychus_grypus', 'oollembola', 'acleridae',
            'aphididae', 'coccidae', 'cydnidae', 'delphacidae', 'pseudococcidae',
            'coleoptera', 'buprestidae', 'paraphaeosphaeria_michotii', 'curvularia_lunata',
            'leaf_hopper', 'army_worm', 'termite', 'black_beetle', 'whitefly',
            'early_shoot_borer', 'sugarcane_scale', 'mites', 'top_shoot_borer',
            'internode_borer', 'stalk_borer', 'grasshopper', 'shoot_boorer',
            'top_boorer', 'root_grub', 'cane_moth', 'cane_weevil', 'cane_mite',
            'earwig', 'cane_bug'
        ]

        # Define all pesticides
        self.pesticides = [
            'thiophanate_methyl', 'carbendazim', 'propiconazole', 'mancozeb',
            'copper_oxychloride', 'imd_178', 'pyron', 'chakrawarti', 'sarvashakti',
            'organic_pest_controller', 'triadimefon', 'chlorpyrifos', 'diazinon',
            'thiamethoxam', 'imidacloprid', 'fipronil', 'bifenthrin', 'oxamyl',
            'fenamiphos', 'quinalphos', 'cypermethrin', 'phorate', 'propargite', 'carbaryl'
        ]

        # Build knowledge base - symptom_of relation used to diagonise diseases on the symptom matches
        self.symptom_of = {
            'red_rot': ['reddened_areas_with_white_patches', 'affected_parenchymatous_tissues',
                        'hollow_cavity_with_grey_mycelium', 'dark_brownish_lesions_on_rind',
                        'necrosis_on_nodal_region', 'cut_ends_show_reddening', 'entire_stool_dries'],
            'smut': ['excessive_tillering_lanky', 'black_whip_structures', 'whip_like_sorus_bearing_structures',
                     'stunted_thin_canes', 'narrow_weak_leaves', 'proliferating_axillary_buds', 'stem_or_leaf_galls'],
            'wilt': ['yellowish_stools_drying', 'dull_brownish_discolouration_internal', 'linear_pith_cavities',
                     'dried_canes_detopped_crown', 'yellowish_foliage'],
            'sett_rot': ['pineapple_odor', 'setts_fail_to_germinate', 'sett_rot_before_germination',
                         'shoot_die_after_emergence', 'stunted_chlorotic_shoots', 'sett_blackening_with_spores',
                         'wilting_and_withering'],
            'ratoon_stunting_disease': ['stunted_growth', 'reduced_tillering', 'thin_stalks_shortened_internodes',
                                        'yellowish_foliage', 'vascular_bundle_discolouration_nodes'],
            'grassy_shoot': ['excessive_tillering_lanky', 'narrow_leaves', 'grass_like_appearance', 'stunted_growth'],
            'mosaic': ['chlorotic_areas_young_leaves', 'yellowish_stripes', 'mild_mottling', 'stunted_growth',
                       'yellowing', 'necrosis'],
            'yellow_leaf_disease': ['yellowish_midrib_lower_surface', 'reddish_pinkish_discolouration_midrib',
                                    'shortening_internodes_top', 'bunching_leaves_top', 'reduced_cane_thickness',
                                    'stunted_growth', 'necrosis', 'yellowing'],
            'pokkah_boeng': ['malformed_twisted_top', 'white_mycelium_on_leaves',
                             'wrinkling_twisting_shortening_leaves',
                             'irregular_reddish_stripes_specks', 'knife_cut_symptoms', 'top_rot'],
            'leaf_fleck': ['flecks_specks_leaf_lamina', 'premature_leaf_drying', 'tiny_chlorotic_flecks',
                           'mottling_on_middle_leaves', 'reddening_and_drying', 'fleck_coalescence',
                           'reduced_plant_vigor'],
            'rust': ['rust_pustules', 'small_chlorotic_puncta', 'brown_tawny_pustules', 'lesion_coalescence',
                     'reduced_canopy_density'],
            'orange_rust': ['orange_powdery_pustules', 'yellow_orange_streaks_on_leaves', 'pustules_between_leaf_veins',
                            'premature_leaf_drying', 'leaf_yellowing', 'reduced_tillering', 'stunted_growth'],
            'eye_spot': ['eye_shaped_spots', 'minute_water_soaked_spots_on_young_leaves',
                         'reddish_brown_elliptical_lesions_parallel_to_veins',
                         'lesions_0_5_to_4_mm_long_with_yellowish_brown_margins',
                         'grey_or_tan_center_in_mature_spots',
                         'reddish_brown_to_yellowish_runners_streaking_toward_leaf_tip',
                         'lesions_may_coalesce_into_long_streaks',
                         'seedling_blight_and_top_rot_in_severe_infections'],
            'brown_spot': ['brown_spots', 'red_brown_oval_or_elliptical_lesions_on_leaf_blade',
                           'lesion_size_approximately_3_to_15_mm', 'narrow_yellow_halo_around_spots',
                           'spots_may_increase_and_coalesce_forming_larger_necrotic_areas',
                           'occurs_from_seedling_stage_through_maturity_under_favourable_conditions'],
            'yellow_spot': ['yellow_spots', 'small_yellow_leaf_lesions_initially',
                            'lesions_enlarge_and_turn_reddish_or_brown_with_age',
                            'splotchy_yellow_lesions_that_may_transition_to_brown',
                            'gray_fuzzy_down_of_conidiophores_often_on_leaf_underside',
                            'visible_from_distance_when_widespread_in_canopy_wet_tropics'],
            'brown_stripe': ['brown_stripes', 'brown_lesions_along_leaf_blades_parallel_to_veins',
                             'narrow_dark_brown_stripes_on_young_leaves',
                             'lesions_may_merge_into_bands_covering_large_leaf_area',
                             'disease_develops_under_warm_humid_conditions'],
            'ring_spot': ['ring_shaped_spots', 'small_elongated_or_oval_spots_dark_olivaceous_green_to_reddish_brown',
                          'narrow_yellow_halo_surrounding_each_spot',
                          'larger_elongated_lesions_2_5_to_5_mm_x_10_to_18_mm_with_red_brown_margins',
                          'spots_coalesce_into_patches_leading_to_leaf_chlorosis_and_necrosis',
                          'small_black_fruiting_bodies_may_be_visible_in_old_lesions'],
            'leaf_blast': ['yellow_narrow_spots_with_long_axes_parallel_to_vessels',
                           'small_yellowish_or_pale_spots_on_leaf_blades_initially',
                           'spots_extend_long_axes_parallel_to_leaf_veins',
                           'lesions_turn_brown_and_merge_into_larger_blighted_areas',
                           'severe_infection_causes_whole_leaf_to_wither_and_dry'],
            'curvularia_leaf_spot': ['slight_pale_yellow_ribbon_on_first_five_leaves', 'red_changes_around_lesion',
                                     'small_to_medium_brown_or_reddish_elliptical_lesions_on_leaves',
                                     'pale_yellow_ribbon_or_band_on_first_few_leaves_of_seedlings',
                                     'red_or_reddish_margin_or_red_changes_around_lesion_center',
                                     'lesions_may_coalesce_and_cause_early_leaf_senescence'],
            'leaf_scald': ['white_stripes_on_leaves', 'leaf_yellowing_from_tip', 'stunted_growth',
                           'cane_death_in_advanced_infection']
        }

        # Build pest_causes_disease relation and used to identify what causes the disease
        self.pest_causes_disease = {
            'colletotrichum_falcatum': ['red_rot'],
            'sporisorium_scitamineum': ['smut'],
            'fusarium_sacchari': ['wilt'],
            'ceratocystis_paradoxa': ['sett_rot'],
            'leifsonia_xyli': ['ratoon_stunting_disease'],
            'sugarcane_grassy_shoot_phytoplasma': ['grassy_shoot'],
            'sugarcane_mosaic_virus': ['mosaic'],
            'sugarcane_yellow_leaf_virus': ['yellow_leaf_disease'],
            'fusarium_verticillioides': ['pokkah_boeng'],
            'fusarium_proliferatum': ['pokkah_boeng'],
            'sugarcane_bacilliform_virus': ['leaf_fleck'],
            'foliar_fungus': ['rust', 'eye_spot', 'brown_spot', 'yellow_spot', 'brown_stripe', 'ring_spot'],
            'xanthomonas_albilineans': ['leaf_scald'],
            'paraphaeosphaeria_michotii': ['leaf_blast'],
            'curvularia_lunata': ['curvularia_leaf_spot']
        }

        # Build pest_causes_effect relation and explains the damage caused by pests
        self.pest_causes_effect = {
            'top_shoot_borer': ['dead_heart', 'tip_wilting', 'suppressed_shoot_growth', 'malformed_leaves',
                                'reduced_tillering', 'shortened_internodes'],
            'white_grub': ['severe_root_pruning', 'poor_nutrient_absorption', 'stunted_growth',
                           'yellowing_of_foliage', 'wilting_even_in_moist_soil', 'plant_toppling'],
            'termite': ['root_damage', 'hollowing_of_stalks', 'plant_collapse', 'dry_rot',
                        'reduced_tillering', 'death_of_young_setts'],
            'mealy_bug': ['honeydew_production', 'sooty_mold_growth', 'sap_sucking',
                          'reduced_photosynthesis', 'internode_shrinkage', 'leaf_yellowing', 'stunted_growth'],
            'nematode': ['root_galling', 'poor_water_absorption', 'nutrient_deficiency', 'stunting',
                         'slender_stalks', 'reduced_root_mass', 'wilting_under_low_stress'],
            'leaf_hopper': ['sap_extraction', 'yellowing_of_leaf_blades', 'leaf_tip_necrosis',
                            'hopperburn_damage', 'virus_transmission', 'reduced_tillering', 'stunted_plants'],
            'stalk_borer': ['tunneling_in_lower_stalk', 'internal_tissue_destruction', 'reduced_juice_content',
                            'increased_fiber_percentage', 'breakage_at_wind', 'lodging', 'poor_cane_quality'],
            'early_shoot_borer': ['dead_heart', 'tunneling_stem', 'shoot_wilting'],
            'internode_borer': ['shortened_internodes', 'borehole_sealing', 'yield_loss'],
            'root_borer': ['dead_heart', 'underground_stalk_damage', 'yield_loss'],
            'whitefly': ['leaf_drying', 'slow_plant_growth', 'discoloration'],
            'grasshopper': ['leaf_spot', 'leaf_blight', 'rust'],
            'shoot_boorer': ['top_rot', 'stem_rot', 'sett_rot'],
            'top_boorer': ['top_rot', 'stem_rot'],
            'root_grub': ['root_rot', 'root_knot', 'sett_rot'],
            'cane_moth': ['stem_rot', 'top_rot', 'red_rot'],
            'cane_weevil': ['root_rot', 'stem_rot', 'root_knot'],
            'cane_mite': ['leaf_scald', 'leaf_spot', 'rust'],
            'earwig': ['sett_rot', 'stunted_shoot'],
            'cane_bug': ['ratoon_stunting', 'leaf_spot', 'gumming_disease']
        }

        # Build pesticide_controls relation treatment recommendation for the pesticide to control that pest
        self.pesticide_controls = {
            'thiophanate_methyl': ['colletotrichum_falcatum', 'ceratocystis_paradoxa'],
            'carbendazim': ['colletotrichum_falcatum', 'ceratocystis_paradoxa'],
            'propiconazole': ['sporisorium_scitamineum'],
            'mancozeb': ['foliar_fungus'],
            'copper_oxychloride': ['foliar_fungus'],
            'imd_178': ['whitefly'],
            'chakrawarti': ['leaf_hopper'],
            'sarvashakti': ['mealy_bug'],
            'organic_pest_controller': ['early_shoot_borer', 'top_shoot_borer'],
            'triadimefon': ['smut'],
            'chlorpyrifos': ['black_beetle', 'termite', 'army_worm', 'sugarcane_scale',
                             'grasshopper', 'shoot_boorer'],
            'imidacloprid': ['cane_bug'],
            'thiamethoxam': [],
            'fipronil': ['top_shoot_borer'],
            'oxamyl': ['nematode'],
            'fenamiphos': ['nematode', 'root_grub'],
            'quinalphos': ['top_boorer'],
            'cypermethrin': ['cane_moth'],
            'phorate': ['cane_weevil'],
            'propargite': ['cane_mite'],
            'carbaryl': ['earwig']
        }

    def diagnose_disease(self, observed_symptoms): # it counts to how many symptoms match each disease and calculates confidence percentage and also ranks the diseases by confidence
        """Diagnose diseases based on observed symptoms"""
        possible_diseases = {}

        for disease, symptoms in self.symptom_of.items():
            match_count = sum(1 for s in observed_symptoms if s in symptoms)
            if match_count > 0:
                confidence = (match_count / len(symptoms)) * 100
                possible_diseases[disease] = {
                    'matches': match_count,
                    'total_symptoms': len(symptoms),
                    'confidence': confidence
                }

        return sorted(possible_diseases.items(), key=lambda x: x[1]['confidence'], reverse=True)

    def identify_pests(self, disease):#maps the diagnosed disease to its pests
        """Identify pests that cause a specific disease"""
        pests = []
        for pest, diseases in self.pest_causes_disease.items():
            if disease in diseases:
                pests.append(pest)
        return pests

    def recommend_pesticides(self, pest):#suggests treatment based on pest
        """Recommend pesticides for a specific pest"""
        pesticides = []
        for pesticide, controlled_pests in self.pesticide_controls.items():
            if pest in controlled_pests:
                pesticides.append(pesticide)
        return pesticides

    def get_pest_effects(self, pest):
        """Get effects caused by a specific pest"""
        return self.pest_causes_effect.get(pest, [])


# Streamlit App
def main():
    st.set_page_config(page_title="Sugarcane Disease Expert System", page_icon="🌾", layout="wide")

    st.title(" SUGARCANE DISEASE EXPERT SYSTEM")
    st.markdown("###  Disease Diagnosis & Treatment Recommendation")
    st.markdown("---")

    # Initialize system
    if 'system' not in st.session_state:
        st.session_state.system = SugarcaneExpertSystem()

    system = st.session_state.system

    # Sidebar
    st.sidebar.header("SYSTEM INFORMATION")
    st.sidebar.info(f"""
    **Knowledge Base:**
    - {len(system.diseases)} Diseases
    - {len(system.symptoms)} Symptoms
    - {len(system.pests)} Pests
    - {len(system.pesticides)} Pesticides
    """)

    st.sidebar.markdown("---")
    st.sidebar.header("ABOUT")
    st.sidebar.markdown("""
    This expert system uses rule-based reasoning to:
    1. Diagnose diseases from symptoms
    2. Identify causative pests
    3. Recommend appropriate pesticides
    """)

    # Main content
    tab1, tab2, tab3 = st.tabs([" Diagnosis", " Knowledge Base", "Help"])

    with tab1:
        st.header("Disease Diagnosis")

        # Symptom selection
        st.subheader("Step 1: Select Observed Symptoms")

        # Search box
        search = st.text_input(" Search symptoms", placeholder="Type to filter symptoms...")

        # Filter symptoms
        if search:
            filtered_symptoms = [s for s in system.symptoms if search.lower() in s.lower()]
        else:
            filtered_symptoms = system.symptoms

        # Multiselect for symptoms
        selected_symptoms = st.multiselect(
            "Select all symptoms you observe:",
            options=filtered_symptoms,
            format_func=lambda x: x.replace('_', ' ').title(),
            help="Select multiple symptoms by clicking on them"
        )

        st.info(f" {len(selected_symptoms)} symptoms selected")

        # Diagnosis button
        if st.button(" Diagnose Disease", type="primary"):
            if not selected_symptoms:
                st.warning(" Please select at least one symptom!")
            else:
                with st.spinner("Analyzing symptoms..."):
                    diseases = system.diagnose_disease(selected_symptoms)

                    if not diseases:
                        st.error(" No diseases matched the observed symptoms.")
                    else:
                        st.success(f"Found {len(diseases)} possible disease(s)")
                        st.markdown("---")

                        # Display results
                        st.subheader(" Diagnosis Results")

                        for i, (disease, info) in enumerate(diseases[:5], 1):
                            with st.expander(
                                    f"**{i}. {disease.replace('_', ' ').upper()}** - Confidence: {info['confidence']:.1f}%",
                                    expanded=(i == 1)):
                                col1, col2 = st.columns([1, 2])

                                with col1:
                                    st.metric("Confidence", f"{info['confidence']:.1f}%")
                                    st.metric("Symptom Match", f"{info['matches']}/{info['total_symptoms']}")

                                with col2:
                                    # Progress bar
                                    st.progress(info['confidence'] / 100)

                                # Identify pests
                                pests = system.identify_pests(disease)
                                if pests:
                                    st.markdown("####  Causative Pests:")
                                    for pest in pests:
                                        st.markdown(f"**• {pest.replace('_', ' ').title()}**")

                                        # Get pest effects
                                        effects = system.get_pest_effects(pest)
                                        if effects:
                                            st.markdown(f"  *Effects:* {', '.join(effects[:3])}")

                                        # Recommend pesticides
                                        pesticides = system.recommend_pesticides(pest)
                                        if pesticides:
                                            st.markdown(
                                                f"   *Recommended Pesticides:* {', '.join([p.replace('_', ' ').title() for p in pesticides])}")

                                        st.markdown("---")

    with tab2:
        st.header(" Knowledge Base Explorer")

        kb_tab1, kb_tab2, kb_tab3, kb_tab4 = st.tabs(["Diseases", "Symptoms", "Pests", "Pesticides"])

        with kb_tab1:
            st.subheader("All Diseases")
            for i, disease in enumerate(system.diseases, 1):
                st.write(f"{i}. {disease.replace('_', ' ').title()}")

        with kb_tab2:
            st.subheader("All Symptoms")
            col1, col2 = st.columns(2)
            mid = len(system.symptoms) // 2
            with col1:
                for i, symptom in enumerate(system.symptoms[:mid], 1):
                    st.write(f"{i}. {symptom.replace('_', ' ').title()}")
            with col2:
                for i, symptom in enumerate(system.symptoms[mid:], mid + 1):
                    st.write(f"{i}. {symptom.replace('_', ' ').title()}")

        with kb_tab3:
            st.subheader("All Pests")
            col1, col2 = st.columns(2)
            mid = len(system.pests) // 2
            with col1:
                for i, pest in enumerate(system.pests[:mid], 1):
                    st.write(f"{i}. {pest.replace('_', ' ').title()}")
            with col2:
                for i, pest in enumerate(system.pests[mid:], mid + 1):
                    st.write(f"{i}. {pest.replace('_', ' ').title()}")

        with kb_tab4:
            st.subheader("All Pesticides")
            for i, pesticide in enumerate(system.pesticides, 1):
                st.write(f"{i}. {pesticide.replace('_', ' ').title()}")

    with tab3:
        st.header("ℹ How to Use This System")

        st.markdown("""
        ### Step-by-Step Guide:

        1. **Select Symptoms** 
           - Go to the "Diagnosis" tab
           - Use the search box to find specific symptoms
           - Select all observed symptoms from the dropdown

        2. **Run Diagnosis**
           - Click the "Diagnose Disease" button
           - The system will analyze symptoms using rule-based reasoning

        3. **Review Results**
           - See possible diseases ranked by confidence
           - View causative pests for each disease
           - Get pesticide recommendations
           - View pest effects

        ### Understanding Confidence Scores:
        - **High (70-100%)**: Strong match - likely diagnosis
        - **Medium (40-69%)**: Moderate match - possible diagnosis
        - **Low (1-39%)**: Weak match - less likely

        ### Tips:
        - Select more symptoms for better accuracy
        - Use the search box to quickly find symptoms
        - Check multiple diseases if symptoms overlap

        ### Example Workflow:
        ```
        Observed: Yellowing, stunted growth, reduced tillering
        ↓
        System analyzes symptoms
        ↓
        Result: Ratoon Stunting Disease (80% confidence)
        ↓
        Pest: Leifsonia xyli
        ↓
        Recommended treatment
        ```
        """)

        st.markdown("---")
        st.success(" **Pro Tip:** The more symptoms you select, the more accurate the diagnosis!")


if __name__ == "__main__":
    main()