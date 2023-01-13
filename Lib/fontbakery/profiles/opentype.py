from fontbakery.fonts_profile import profile_factory  # NOQA pylint: disable=unused-import
from fontbakery.section import Section

OPENTYPE_PROFILE_IMPORTS = (
    ".",
    (
        "cff",
        "cmap",
        "head",
        "os2",
        "post",
        "name",
        "loca",
        "hhea",
        "dsig",
        "gdef",
        "gpos",
        "kern",
        "glyf",
        "fvar",
        "stat",
        "layout",
        "shared_conditions",
    ),
)
profile_imports = (OPENTYPE_PROFILE_IMPORTS, )
profile = profile_factory(default_section=Section("OpenType Specification Checks"))

OPENTYPE_PROFILE_CHECKS = [
    'com.google.fonts/check/family/underline_thickness',
    'com.google.fonts/check/family/panose_proportion',
    'com.google.fonts/check/family/panose_familytype',
    'com.google.fonts/check/family/equal_unicode_encodings',
    'com.google.fonts/check/family/equal_font_versions',
    'com.adobe.fonts/check/family/bold_italic_unique_for_nameid1',
    'com.adobe.fonts/check/family/max_4_fonts_per_family_name',
    'com.adobe.fonts/check/name/postscript_vs_cff',
    'com.adobe.fonts/check/name/postscript_name_consistency',
    'com.adobe.fonts/check/name/empty_records',
    'com.google.fonts/check/name/no_copyright_on_description',
    'com.google.fonts/check/name/match_familyname_fullfont',
    'com.google.fonts/check/varfont/regular_wght_coord',
    'com.google.fonts/check/varfont/regular_wdth_coord',
    'com.google.fonts/check/varfont/regular_slnt_coord',
    'com.google.fonts/check/varfont/regular_ital_coord',
    'com.google.fonts/check/varfont/regular_opsz_coord',
    'com.google.fonts/check/varfont/bold_wght_coord',
    'com.google.fonts/check/varfont/slnt_range',
    'com.google.fonts/check/varfont/wght_valid_range',
    'com.google.fonts/check/varfont/wdth_valid_range',
    'com.google.fonts/check/varfont/stat_axis_record_for_each_axis',
    'com.google.fonts/check/loca/maxp_num_glyphs',
    'com.adobe.fonts/check/cff2_call_depth',
    'com.adobe.fonts/check/cff_call_depth',
    'com.adobe.fonts/check/cff_deprecated_operators',
    'com.google.fonts/check/font_version',
    'com.google.fonts/check/post_table_version',
    'com.google.fonts/check/monospace',
    'com.google.fonts/check/xavgcharwidth',
    'com.adobe.fonts/check/fsselection_matches_macstyle',
    'com.google.fonts/check/linegaps',
    'com.google.fonts/check/unitsperem',
    'com.google.fonts/check/dsig',
    'com.google.fonts/check/gdef_spacing_marks',
    'com.google.fonts/check/gdef_mark_chars',
    'com.google.fonts/check/gdef_non_mark_chars',
    'com.google.fonts/check/gpos_kerning_info',
    'com.google.fonts/check/kern_table',
    'com.google.fonts/check/glyf_unused_data',
    'com.google.fonts/check/family_naming_recommendations',
    'com.google.fonts/check/maxadvancewidth',
    'com.google.fonts/check/points_out_of_bounds',
    'com.google.fonts/check/glyf_non_transformed_duplicate_components',
    'com.google.fonts/check/code_pages',
    'com.google.fonts/check/layout_valid_feature_tags',
    'com.google.fonts/check/layout_valid_script_tags',
    'com.google.fonts/check/layout_valid_language_tags',
    'com.google.fonts/check/italic_angle',
    'com.google.fonts/check/mac_style',
    'com.google.fonts/check/fsselection',
    'com.google.fonts/check/name/italic_names',
    'com.adobe.fonts/check/varfont/valid_axis_nameid',
    'com.adobe.fonts/check/varfont/valid_subfamily_nameid',
    'com.adobe.fonts/check/varfont/valid_postscript_nameid',
    'com.adobe.fonts/check/varfont/valid_default_instance_nameids',
    'com.adobe.fonts/check/varfont/same_size_instance_records',
    'com.adobe.fonts/check/varfont/distinct_instance_records',
    'com.adobe.fonts/check/stat_has_axis_value_tables',
    'com.thetypefounders/check/vendor_id',
]

profile.auto_register(globals())
profile.test_expected_checks(OPENTYPE_PROFILE_CHECKS, exclusive=True)
