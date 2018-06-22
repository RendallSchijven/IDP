import sys

sys.path.insert(0, '../../../../src')

stair_2 = [
    [
        [654, 287, 767],
        [368, 296, 759],
        [654, 287, 767],
        [368, 296, 759]
    ],
    [
        [654, 579, 674],
        [367, 557, 674],
        [654, 579, 674],
        [367, 557, 674]
    ]

]

stair = [
    # Laag begin
    [
        [310, 170, 890],  # L voor
        [790, 170, 890],  # R voor
        [310, 170, 890],  # L achter
        [790, 170, 890]  # R achter
    ],
    # Laag eind
    [
        [360, 170, 890],  # L voor
        [790, 350, 890],  # R voor
        [360, 170, 890],  # L achter
        [790, 350, 890]  # R achter
    ],
    # Hoog begin
    [
        [360, 350, 890],  # L voor
        [750, 350, 890],  # R voor
        [360, 350, 890],  # L achter
        [750, 350, 890]  # R achter
    ],
    # Hoog eind
    [
        [310, 350, 890],  # L voor
        [750, 170, 890],  # R voor
        [310, 350, 890],  # L achter
        [750, 170, 890]  # R achter
    ]
]

clap = [
    [
        [736, 469, 840],
        [287, 459, 840],
        [736, 469, 840],
        [287, 459, 840]
    ],
    [
        [608, 433, 863],
        [410, 460, 845],
        [608, 433, 863],
        [410, 460, 845]
    ]
]

forward = [
    [
        [630, 266, 850],
        [430, 266, 850],
        [530, 266, 850],
        [530, 266, 850]
    ],
    [
        [530, 266, 850],
        [530, 266, 850],
        [530, 266, 850],
        [530, 266, 850]
    ],
    [
        [530, 266, 850],
        [530, 266, 850],
        [630, 266, 850],
        [430, 266, 850]
    ],
    [
        [530, 266, 850],
        [530, 266, 850],
        [530, 266, 850],
        [530, 266, 850]
    ]

]

backward = [
    [
        [630, 266, 850],
        [630, 266, 850],
        [630, 266, 850],
        [630, 266, 850]
    ],
    [
        [630, 200, 850],
        [630, 200, 850],
        [630, 200, 850],
        [630, 200, 850]
    ],
    [
        [530, 200, 850],
        [530, 200, 850],
        [530, 200, 850],
        [530, 200, 850]
    ],
    [
        [530, 266, 850],
        [530, 266, 850],
        [530, 266, 850],
        [530, 266, 850]
    ]
]

dab = [
    [
        [315, 178, 1023],
        [315, 178, 1023],
        [315, 178, 1023],
        [315, 178, 1023]
    ]
]

wave = [
    [
        [527, 180, 998],
        [527, 180, 998],
        [527, 180, 998],
        [527, 180, 998]
    ],
    [
        [527, 250, 900],
        [527, 250, 900],
        [527, 250, 900],
        [527, 250, 900]
    ]
]

pull = [
    [
        [530, 230, 640],
        [530, 230, 640],
        [530, 230, 640],
        [530, 230, 640]
    ],
    [
        [530, 150, 640],
        [530, 150, 640],
        [530, 150, 640],
        [530, 150, 640]
    ],
    [
        [530, 150, 750],
        [530, 150, 750],
        [530, 150, 750],
        [530, 150, 750]
    ],
    [
        [530, 340, 970],
        [530, 340, 970],
        [530, 340, 970],
        [530, 340, 970]
    ]
]

push = [
    [
        [530, 150, 750],
        [530, 150, 750],
        [530, 150, 750],
        [530, 150, 750]
    ],
    [
        [530, 150, 640],
        [530, 150, 640],
        [530, 150, 640],
        [530, 150, 640]

    ],
    [
        [530, 230, 640],
        [530, 230, 640],
        [530, 230, 640],
        [530, 230, 640]
    ],
    [
        [530, 340, 970],
        [530, 340, 970],
        [530, 340, 970],
        [530, 340, 970]
    ]
]

march = [
    [
        [530, 100, 570],
        [530, 100, 570],
        [530, 100, 570],
        [530, 100, 570]
    ],
    [
        [530, 230, 690],
        [530, 230, 690],
        [530, 230, 690],
        [530, 230, 690]
    ]
]

hood_handshake = [
    [
        [530, 180, 950],
        [530, 180, 950],
        [530, 180, 950],
        [530, 180, 950]
    ],
    [
        [420, 180, 950],
        [420, 180, 950],
        [420, 180, 950],
        [420, 180, 950]
    ],
    [
        [640, 180, 950],
        [640, 180, 950],
        [640, 180, 950],
        [640, 180, 950]
    ],
    [
        [530, 180, 950],
        [530, 180, 950],
        [530, 180, 950],
        [530, 180, 950]
    ],
    [
        [530, 830, 855],
        [530, 830, 855],
        [530, 830, 855],
        [530, 830, 855]
    ],
    [
        [530, 940, 790],
        [530, 940, 790],
        [530, 940, 790],
        [530, 940, 790]
    ],
    [
        [530, 830, 855],
        [530, 830, 855],
        [530, 830, 855],
        [530, 830, 855]
    ],
    [
        [530, 800, 580],
        [530, 800, 580],
        [530, 800, 580],
        [530, 800, 580]
    ],
    [
        [530, 1020, 800],
        [530, 1020, 800],
        [530, 1020, 800],
        [530, 1020, 800]
    ],
    [
        [530, 700, 470],
        [530, 700, 470],
        [530, 700, 470],
        [530, 700, 470]
    ]
]
