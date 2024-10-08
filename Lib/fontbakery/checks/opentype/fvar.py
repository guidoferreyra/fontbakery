from fontbakery.callable import check
from fontbakery.constants import REGISTERED_AXIS_TAGS
from fontbakery.status import FAIL, PASS, WARN, SKIP
from fontbakery.message import Message


@check(
    id="opentype/varfont/regular_wght_coord",
    rationale="""
        According to the Open-Type spec's
        registered design-variation tag 'wght' available at
        https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght

        If a variable font has a 'wght' (Weight) axis, then the coordinate of
        its 'Regular' instance is required to be 400.
    """,
    conditions=["is_variable_font", "has_wght_axis"],
    proposal="https://github.com/fonttools/fontbakery/issues/1707",
)
def check_varfont_regular_wght_coord(ttFont, regular_wght_coord):
    """The variable font 'wght' (Weight) axis coordinate must be 400 on the
    'Regular' instance."""

    if regular_wght_coord is None:
        yield FAIL, Message("no-regular-instance", '"Regular" instance not present.')
    elif regular_wght_coord == 400:
        yield PASS, "Regular:wght is 400."
    else:
        yield FAIL, Message(
            "wght-not-400",
            f'The "wght" axis coordinate of'
            f' the "Regular" instance must be 400.'
            f" Got {regular_wght_coord} instead.",
        )


@check(
    id="opentype/varfont/regular_wdth_coord",
    rationale="""
        According to the Open-Type spec's
        registered design-variation tag 'wdth' available at
        https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wdth

        If a variable font has a 'wdth' (Width) axis, then the coordinate of
        its 'Regular' instance is required to be 100.
    """,
    conditions=["is_variable_font", "has_wdth_axis"],
    proposal="https://github.com/fonttools/fontbakery/issues/1707",
)
def check_varfont_regular_wdth_coord(ttFont, regular_wdth_coord):
    """
    The variable font 'wdth' (Width) axis coordinate must be 100 on the 'Regular'
    instance.
    """

    if regular_wdth_coord is None:
        yield FAIL, Message("no-regular-instance", '"Regular" instance not present.')
    elif regular_wdth_coord == 100:
        yield PASS, "Regular:wdth is 100."
    else:
        yield FAIL, Message(
            "wdth-not-100",
            f'The "wdth" axis coordinate of'
            f' the "Regular" instance must be 100.'
            f" Got {regular_wdth_coord} as a default value instead.",
        )


@check(
    id="opentype/varfont/regular_slnt_coord",
    rationale="""
        According to the Open-Type spec's
        registered design-variation tag 'slnt' available at
        https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_slnt

        If a variable font has a 'slnt' (Slant) axis, then the coordinate of
        its 'Regular' instance is required to be zero.
    """,
    conditions=["is_variable_font", "has_slnt_axis"],
    proposal="https://github.com/fonttools/fontbakery/issues/1707",
)
def check_varfont_regular_slnt_coord(ttFont, regular_slnt_coord):
    """
    The variable font 'slnt' (Slant) axis coordinate must be zero on the 'Regular'
    instance.
    """

    if regular_slnt_coord is None:
        yield FAIL, Message("no-regular-instance", '"Regular" instance not present.')
    elif regular_slnt_coord == 0:
        yield PASS, "Regular:slnt is zero."
    else:
        yield FAIL, Message(
            "slnt-not-0",
            f'The "slnt" axis coordinate of'
            f' the "Regular" instance must be zero.'
            f" Got {regular_slnt_coord} as a default value instead.",
        )


@check(
    id="opentype/varfont/regular_ital_coord",
    rationale="""
        According to the Open-Type spec's
        registered design-variation tag 'ital' available at
        https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_ital

        If a variable font has a 'ital' (Italic) axis, then the coordinate of
        its 'Regular' instance is required to be zero.
    """,
    conditions=["is_variable_font", "has_ital_axis"],
    proposal="https://github.com/fonttools/fontbakery/issues/1707",
)
def check_varfont_regular_ital_coord(ttFont, regular_ital_coord):
    """
    The variable font 'ital' (Italic) axis coordinate must be zero on the 'Regular'
    instance.
    """

    if regular_ital_coord is None:
        yield FAIL, Message("no-regular-instance", '"Regular" instance not present.')
    elif regular_ital_coord == 0:
        yield PASS, "Regular:ital is zero."
    else:
        yield FAIL, Message(
            "ital-not-0",
            f'The "ital" axis coordinate of'
            f' the "Regular" instance must be zero.'
            f" Got {regular_ital_coord} as a default value instead.",
        )


@check(
    id="opentype/varfont/regular_opsz_coord",
    rationale="""
        According to the Open-Type spec's
        registered design-variation tag 'opsz' available at
        https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_opsz

        If a variable font has an 'opsz' (Optical Size) axis, then
        the coordinate of its 'Regular' instance is recommended to be
        a value in the range 10 to 16.
    """,
    conditions=["is_variable_font", "has_opsz_axis"],
    proposal="https://github.com/fonttools/fontbakery/issues/1707",
)
def check_varfont_regular_opsz_coord(ttFont, regular_opsz_coord):
    """
    The variable font 'opsz' (Optical Size) axis coordinate should be between 10 and 16
    on the 'Regular' instance.
    """

    if regular_opsz_coord is None:
        yield FAIL, Message("no-regular-instance", '"Regular" instance not present.')
    elif regular_opsz_coord >= 10 and regular_opsz_coord <= 16:
        yield PASS, f"Regular:opsz coordinate ({regular_opsz_coord}) looks good."
    else:
        yield WARN, Message(
            "opsz-out-of-range",
            f'The "opsz" (Optical Size) coordinate'
            f' on the "Regular" instance is recommended'
            f" to be a value in the range 10 to 16."
            f" Got {regular_opsz_coord} instead.",
        )


@check(
    id="opentype/varfont/wght_valid_range",
    rationale="""
        According to the Open-Type spec's
        registered design-variation tag 'wght' available at
        https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght

        On the 'wght' (Weight) axis, the valid coordinate range is 1-1000.
    """,
    conditions=["is_variable_font", "has_wght_axis"],
    proposal="https://github.com/fonttools/fontbakery/issues/2264",
)
def check_varfont_wght_valid_range(ttFont):
    """The variable font 'wght' (Weight) axis coordinate
    must be within spec range of 1 to 1000 on all instances."""

    for instance in ttFont["fvar"].instances:
        if "wght" in instance.coordinates:
            value = instance.coordinates["wght"]
            if value < 1 or value > 1000:
                yield FAIL, Message(
                    "wght-out-of-range",
                    f'Found a bad "wght" coordinate with value {value}'
                    f" outside of the valid range from 1 to 1000.",
                )
                break


@check(
    id="opentype/varfont/wdth_valid_range",
    rationale="""
        According to the Open-Type spec's
        registered design-variation tag 'wdth' available at
        https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wdth

        On the 'wdth' (Width) axis, the valid numeric range is strictly greater than
        zero.
    """,
    conditions=["is_variable_font", "has_wdth_axis"],
    proposal="https://github.com/fonttools/fontbakery/pull/2520",
)
def check_varfont_wdth_valid_range(ttFont):
    """The variable font 'wdth' (Width) axis coordinate
    must strictly greater than zero."""

    for instance in ttFont["fvar"].instances:
        if "wdth" in instance.coordinates:
            value = instance.coordinates["wdth"]
            if value < 1:
                yield FAIL, Message(
                    "wdth-out-of-range",
                    f'Found a bad "wdth" coordinate with value {value}'
                    f" outside of the valid range (> 0).",
                )
                break

            if value > 1000:
                yield WARN, Message(
                    "wdth-greater-than-1000",
                    f'Found a "wdth" coordinate with value {value}'
                    f" which is valid but unusual.",
                )
                break


@check(
    id="opentype/varfont/slnt_range",
    rationale="""
        The OpenType spec says at
        https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxistag_slnt that:

        [...] the scale for the Slant axis is interpreted as the angle of slant
        in counter-clockwise degrees from upright. This means that a typical,
        right-leaning oblique design will have a negative slant value. This matches
        the scale used for the italicAngle field in the post table.
    """,
    conditions=["is_variable_font", "has_slnt_axis"],
    proposal="https://github.com/fonttools/fontbakery/issues/2572",
)
def check_varfont_slnt_range(ttFont, slnt_axis):
    """The variable font 'slnt' (Slant) axis coordinate
    specifies positive values in its range?"""

    if not (slnt_axis.minValue < 0 and slnt_axis.maxValue >= 0):
        yield WARN, Message(
            "unusual-slnt-range",
            f'The range of values for the "slnt" axis in'
            f" this font only allows positive coordinates"
            f" (from {slnt_axis.minValue} to {slnt_axis.maxValue}),"
            f" indicating that this may be a back slanted design,"
            f" which is rare. If that's not the case, then"
            f' the "slant" axis should be a range of'
            f" negative values instead.",
        )


@check(
    id="opentype/varfont/ital_range",
    rationale="""
        The OpenType spec says at
        https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxistag_ital
        that:

        [...] Valid numeric range: Values must be in the range 0 to 1.
    """,
    conditions=["is_variable_font", "has_ital_axis"],
)
def check_varfont_ital_range(ttFont, ital_axis):
    """The variable font 'ital' (Italic) axis coordinates
    is in a valid range?"""

    if not (ital_axis.minValue == 0 and ital_axis.maxValue == 1):
        yield FAIL, Message(
            "invalid-ital-range",
            f'The range of values for the "ital" axis in'
            f" this font is {ital_axis.minValue} to {ital_axis.maxValue}."
            f" Italic axis range must be 0 to 1, "
            f" where Roman is 0 and Italic 1."
            f" If you prefer a bigger variation range consider using"
            f' "Slant" axis instead of "Italic".',
        )


@check(
    id="opentype/varfont/valid_axis_nameid",
    rationale="""
        According to the 'fvar' documentation in OpenType spec v1.9
        https://docs.microsoft.com/en-us/typography/opentype/spec/fvar

        The axisNameID field provides a name ID that can be used to obtain strings
        from the 'name' table that can be used to refer to the axis in application
        user interfaces. The name ID must be greater than 255 and less than 32768.
    """,
    conditions=["is_variable_font"],
    proposal="https://github.com/fonttools/fontbakery/issues/3702",
)
def check_varfont_valid_axis_nameid(ttFont, has_name_table):
    """Validates that the value of axisNameID used by each VariationAxisRecord
    is greater than 255 and less than 32768."""

    if not has_name_table:
        yield FAIL, Message("lacks-table", "Font lacks 'name' table.")
        return

    name_table = ttFont["name"]
    font_axis_nameids = [axis.axisNameID for axis in ttFont["fvar"].axes]
    invalid_axis_nameids = [val for val in font_axis_nameids if not (255 < val < 32768)]

    for nameid in invalid_axis_nameids:
        inst_name = name_table.getDebugName(nameid) or "Unnamed"

        yield FAIL, Message(
            f"invalid-axis-nameid:{nameid}",
            f"{inst_name!r} instance has an axisNameID value that"
            " is not greater than 255 and less than 32768.",
        )


@check(
    id="opentype/varfont/valid_subfamily_nameid",
    rationale="""
        According to the 'fvar' documentation in OpenType spec v1.9
        https://docs.microsoft.com/en-us/typography/opentype/spec/fvar

        The subfamilyNameID field provides a name ID that can be used to obtain
        strings from the 'name' table that can be treated as equivalent to name
        ID 17 (typographic subfamily) strings for the given instance. Values of
        2 or 17 can be used; otherwise, values must be greater than 255 and less
        than 32768.
    """,
    conditions=["is_variable_font"],
    proposal="https://github.com/fonttools/fontbakery/issues/3703",
)
def check_varfont_valid_subfamily_nameid(ttFont, has_name_table):
    """Validates that the value of subfamilyNameID used by each InstanceRecord
    is 2, 17, or greater than 255 and less than 32768."""

    if not has_name_table:
        yield FAIL, Message("lacks-table", "Font lacks 'name' table.")
        return

    name_table = ttFont["name"]
    font_subfam_nameids = [inst.subfamilyNameID for inst in ttFont["fvar"].instances]
    invalid_subfam_nameids = [
        val
        for val in font_subfam_nameids
        if not (255 < val < 32768) and val not in {2, 17}
    ]

    for nameid in invalid_subfam_nameids:
        inst_name = name_table.getDebugName(nameid) or "Unnamed"

        yield FAIL, Message(
            f"invalid-subfamily-nameid:{nameid}",
            f"{inst_name!r} instance has a subfamilyNameID value that"
            " is neither 2, 17, or greater than 255 and less than 32768.",
        )


@check(
    id="opentype/varfont/valid_postscript_nameid",
    rationale="""
        According to the 'fvar' documentation in OpenType spec v1.9
        https://docs.microsoft.com/en-us/typography/opentype/spec/fvar

        The postScriptNameID field provides a name ID that can be used to obtain
        strings from the 'name' table that can be treated as equivalent to name
        ID 6 (PostScript name) strings for the given instance. Values of 6 and
        0xFFFF can be used; otherwise, values must be greater than 255 and less
        than 32768.
    """,
    conditions=["is_variable_font"],
    proposal="https://github.com/fonttools/fontbakery/issues/3704",
)
def check_varfont_valid_postscript_nameid(ttFont, has_name_table):
    """Validates that the value of postScriptNameID used by each InstanceRecord
    is 6, 0xFFFF, or greater than 255 and less than 32768."""

    if not has_name_table:
        yield FAIL, Message("lacks-table", "Font lacks 'name' table.")
        return

    name_table = ttFont["name"]
    font_postscript_nameids = [
        inst.postscriptNameID for inst in ttFont["fvar"].instances
    ]
    invalid_postscript_nameids = [
        val
        for val in font_postscript_nameids
        if not (255 < val < 32768) and val not in {6, 0xFFFF}
    ]

    for nameid in invalid_postscript_nameids:
        inst_name = name_table.getDebugName(nameid) or "Unnamed"

        yield FAIL, Message(
            f"invalid-postscript-nameid:{nameid}",
            f"{inst_name!r} instance has a postScriptNameID value that"
            f" is neither 6, 0xFFFF, or greater than 255 and less than 32768.",
        )


@check(
    id="opentype/varfont/valid_default_instance_nameids",
    rationale="""
        According to the 'fvar' documentation in OpenType spec v1.9.1
        https://docs.microsoft.com/en-us/typography/opentype/spec/fvar

        The default instance of a font is that instance for which the coordinate
        value of each axis is the defaultValue specified in the corresponding
        variation axis record. An instance record is not required for the default
        instance, though an instance record can be provided. When enumerating named
        instances, the default instance should be enumerated even if there is no
        corresponding instance record. If an instance record is included for the
        default instance (that is, an instance record has coordinates set to default
        values), then the nameID value should be set to either 2 or 17 or to a
        name ID with the same value as name ID 2 or 17. Also, if a postScriptNameID is
        included in instance records, and the postScriptNameID value should be set
        to 6 or to a name ID with the same value as name ID 6.
    """,
    conditions=["is_variable_font"],
    proposal="https://github.com/fonttools/fontbakery/issues/3708",
)
def check_varfont_valid_default_instance_nameids(ttFont, has_name_table):
    """Validates that when an instance record is included for the default instance,
    its subfamilyNameID value is set to a name ID whose string is equal to the
    string of either name ID 2 or 17, and its postScriptNameID value is set to a
    name ID whose string is equal to the string of name ID 6."""

    if not has_name_table:
        yield FAIL, Message("lacks-table", "Font lacks 'name' table.")
        return

    name_table = ttFont["name"]
    fvar_table = ttFont["fvar"]

    font_includes_ps_nameid = any(
        inst.postscriptNameID != 0xFFFF for inst in fvar_table.instances
    )
    axes_dflt_coords = {axis.axisTag: axis.defaultValue for axis in fvar_table.axes}
    name2 = name_table.getDebugName(2)
    name6 = name_table.getDebugName(6)
    name17 = name_table.getDebugName(17)
    font_subfam_name = name17 or name2

    for i, inst in enumerate(fvar_table.instances, 1):
        inst_coords = dict(inst.coordinates.items())

        # The instance record has the same coordinates as the default instance
        if inst_coords == axes_dflt_coords:
            subfam_nameid = inst.subfamilyNameID
            subfam_name = name_table.getDebugName(subfam_nameid) or f"Instance #{i}"
            postscript_nameid = inst.postscriptNameID
            postscript_name = name_table.getDebugName(postscript_nameid) or "None"

            # Special handle the 0xFFFF case, to avoid displaying the value as 65535
            if postscript_nameid == 0xFFFF:
                postscript_nameid = "0xFFFF"

            if name17 and subfam_name != font_subfam_name:
                yield FAIL, Message(
                    "invalid-default-instance-subfamily-name",
                    f"{subfam_name!r} instance has the same coordinates as the default"
                    f" instance; its subfamily name should be {font_subfam_name!r}.\n\n"
                    f"Note: It is alternatively possible that Name ID 17 is incorrect,"
                    f" and should be set to the default instance subfamily name, {subfam_name!r},"
                    f" rather than '{name17!r}'. If the default instance is {subfam_name!r},"
                    f" NameID 17 is probably the problem.",
                )

            if not name17 and subfam_name != font_subfam_name:
                yield FAIL, Message(
                    "invalid-default-instance-subfamily-name",
                    f"{subfam_name!r} instance has the same coordinates as the default"
                    f" instance; its subfamily name should be {font_subfam_name!r}.\n\n"
                    f"Note: If the default instance really is meant to be called {subfam_name!r},"
                    f" the problem may be that the font lacks NameID 17, which should"
                    f" probably be present and set to {subfam_name!r}.",
                )

            # Validate the postScriptNameID string only if
            # at least one instance record includes it
            if font_includes_ps_nameid and postscript_name != name6:
                yield FAIL, Message(
                    "invalid-default-instance-postscript-name",
                    f"{subfam_name!r} instance has the same coordinates as the default"
                    f" instance; its postscript name should be {name6!r}, instead of"
                    f" {postscript_name!r}.",
                )


@check(
    id="opentype/varfont/same_size_instance_records",
    rationale="""
        According to the 'fvar' documentation in OpenType spec v1.9
        https://docs.microsoft.com/en-us/typography/opentype/spec/fvar

        All of the instance records in a given font must be the same size, with
        all either including or omitting the postScriptNameID field. [...]
        If the value is 0xFFFF, then the value is ignored, and no PostScript name
        equivalent is provided for the instance.
    """,
    conditions=["is_variable_font"],
    proposal="https://github.com/fonttools/fontbakery/issues/3705",
)
def check_varfont_same_size_instance_records(ttFont):
    """Validates that all of the instance records in a given font have the same size."""

    if not ttFont["fvar"].instances:
        yield SKIP, Message("no-instance-records", "Font has no instance records.")
        return

    font_ps_nameids_not_provided = set(
        inst.postscriptNameID == 0xFFFF for inst in ttFont["fvar"].instances
    )

    # 'font_ps_nameids_not_provided' is a set whose values can only be
    # {True}, {False}, or {True, False}. So if the size of the set is not 1,
    # it means that some instance records have postscriptNameID values while
    # others do not.
    if len(font_ps_nameids_not_provided) != 1:
        yield FAIL, Message(
            "different-size-instance-records",
            "Instance records don't all have the same size.",
        )


@check(
    id="opentype/varfont/distinct_instance_records",
    rationale="""
        According to the 'fvar' documentation in OpenType spec v1.9
        https://docs.microsoft.com/en-us/typography/opentype/spec/fvar

        All of the instance records in a font should have distinct coordinates
        and distinct subfamilyNameID and postScriptName ID values. If two or more
        records share the same coordinates, the same nameID values or the same
        postScriptNameID values, then all but the first can be ignored.
    """,
    conditions=["is_variable_font"],
    proposal="https://github.com/fonttools/fontbakery/issues/3706",
)
def check_varfont_distinct_instance_records(ttFont, has_name_table):
    """Validates that all of the instance records in a given font have distinct data."""

    if not has_name_table:
        yield FAIL, Message("lacks-table", "Font lacks 'name' table.")
        return

    name_table = ttFont["name"]
    unique_inst_recs = set()

    for i, inst in enumerate(ttFont["fvar"].instances, 1):
        inst_coords = list(inst.coordinates.items())
        inst_subfam_nameid = inst.subfamilyNameID
        inst_postscript_nameid = inst.postscriptNameID
        inst_data = (tuple(inst_coords), inst_subfam_nameid, inst_postscript_nameid)

        if inst_data not in unique_inst_recs:
            unique_inst_recs.add(inst_data)

        else:  # non-unique instance was found
            inst_name = name_table.getDebugName(inst_subfam_nameid)

            if inst_name is None:
                inst_name = f"Instance #{i}"

            yield WARN, Message(
                f"repeated-instance-record:{inst_name}",
                f"{inst_name!r} is a repeated instance record.",
            )


@check(
    id="opentype/varfont/foundry_defined_tag_name",
    rationale="""
        According to the Open-Type spec's syntactic requirements for
        foundry-defined design-variation axis tags available at
        https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg

        Foundry-defined tags must begin with an uppercase letter
        and must use only uppercase letters or digits.
    """,
    conditions=["is_variable_font"],
    proposal="https://github.com/fonttools/fontbakery/issues/4043",
)
def check_varfont_foundry_defined_tag_name(ttFont):
    "Validate foundry-defined design-variation axis tag names."
    for axis in ttFont["fvar"].axes:
        axisTag = axis.axisTag
        if axisTag in REGISTERED_AXIS_TAGS:
            continue
        if axisTag.lower() in REGISTERED_AXIS_TAGS:
            yield WARN, Message(
                "foundry-defined-similar-registered-name",
                f'Foundry-defined tag "{axisTag}" is very similar to'
                f' registered tag "{axisTag.lower()}", consider renaming.\n'
                f"If this tag was meant to be a registered tag, please"
                f" use all lowercase letters in the tag name.",
            )

        firstChar = ord(axisTag[0])
        if not (firstChar >= ord("A") and firstChar <= ord("Z")):
            yield FAIL, Message(
                "invalid-foundry-defined-tag-first-letter",
                f'Please fix axis tag "{axisTag}".\n'
                f"Foundry-defined tags must begin with an uppercase letter.",
            )

        for i in range(3):
            char = ord(axisTag[1 + i])
            if not (
                (char >= ord("0") and char <= ord("9"))
                or (char >= ord("A") and char <= ord("Z"))
            ):
                yield FAIL, Message(
                    "invalid-foundry-defined-tag-chars",
                    f'Please fix axis tag "{axisTag}".\n'
                    f"Foundry-defined tags must only use"
                    f" uppercase or digits.",
                )


@check(
    id="opentype/varfont/family_axis_ranges",
    rationale="""
        Between members of a family (such as Roman & Italic),
        the ranges of variable axes must be identical.
    """,
    proposal="https://github.com/fonttools/fontbakery/issues/4445",
    conditions=["VFs"],
)
def check_varfont_family_axis_ranges(ttFonts):
    """Check that family axis ranges are indentical"""

    def axis_info(ttFont):
        if "fvar" in ttFont:
            fvar = ttFont["fvar"]
            axis_info = [
                (a.axisTag, a.minValue, a.maxValue, a.defaultValue) for a in fvar.axes
            ]
            return tuple(sorted(axis_info))

    axes_info_from_font_files = {axis_info(ttFont) for ttFont in ttFonts}
    if len(axes_info_from_font_files) != 1:
        yield FAIL, Message(
            "axis-range-mismatch",
            "Variable axes ranges not matching between font files",
        )


@check(
    id="opentype/slant_direction",
    conditions=["is_variable_font"],
    rationale="""
        The 'slnt' axis values are defined as negative values for a clockwise (right)
        lean, and positive values for counter-clockwise lean. This is counter-intuitive
        for many designers who are used to think of a positive slant as a lean to
        the right.

        This check ensures that the slant axis direction is consistent with the specs.

        https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxistag_slnt
    """,
    proposal="https://github.com/fonttools/fontbakery/pull/3910",
)
def check_slant_direction(ttFont, uharfbuzz_blob):
    """Checking direction of slnt axis angles."""
    import uharfbuzz as hb
    from fontbakery.utils import PointsPen, axis

    if not axis(ttFont, "slnt"):
        yield PASS, "Font has no slnt axis"
        return

    hb_face = hb.Face(uharfbuzz_blob)
    hb_font = hb.Font(hb_face)
    buf = hb.Buffer()
    buf.add_str("H")
    features = {"kern": True, "liga": True}
    hb.shape(hb_font, buf, features)

    def x_delta(slant):
        """
        Return the x delta (difference of x position between highest and lowest point)
        for the given slant value.
        """
        hb_font.set_variations({"slnt": slant})
        pen = PointsPen()
        hb_font.draw_glyph_with_pen(buf.glyph_infos[0].codepoint, pen)
        x_delta = pen.highestPoint()[0] - pen.lowestPoint()[0]
        return x_delta

    if x_delta(axis(ttFont, "slnt").minValue) < x_delta(axis(ttFont, "slnt").maxValue):
        yield FAIL, Message(
            "positive-value-for-clockwise-lean",
            "The right-leaning glyphs have a positive 'slnt' axis value,"
            " which is likely a mistake. It needs to be negative"
            " to lean rightwards.",
        )
