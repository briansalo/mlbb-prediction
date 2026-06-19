UPPER_BRACKETS = [
    "upper_quarter_final",
    "upper_semi_final",
    "upper_final",
]

LOWER_BRACKETS = [
    "lower_semi_final",
    "lower_final",
]

PRELOAD_BRACKETS = {
    "upper_semi_final": [
        "upper_quarter_final",
    ],

    "upper_final": [
        "upper_quarter_final",
        "upper_semi_final",
    ],

    "lower_semi_final": [
        "upper_quarter_final",
        "upper_semi_final",
    ],

    "lower_final": [
        "upper_quarter_final",
        "upper_semi_final",
        "upper_final",
        "lower_semi_final",
    ],

    "grand_final": [
        "upper_quarter_final",
        "upper_semi_final",
        "upper_final",
        "lower_semi_final",
        "lower_final",
    ],
}