"""Hand-reviewed panel tags for published Stories 1-2 of Adventures with the Bull.

Every entry was assigned by visually reviewing all 130 published images
(Nov 18 2026) against the manuscript text surrounding each panel.

Panel ids are ``(story, n)`` where ``story`` is 1 or 2 and ``n`` is the 1-based
position of the panel in the Sanity ``body`` array (``S1-p05`` in prose).

Entry format: ``(story, n, role, note)``
  role  -- "hero" (best canonical likeness), "ok" (usable reference),
           "detail" (partial / back view / hands only),
           "offmodel" (deliberately departs from canon -- do not use as likeness ref)
  note  -- short human-readable context
"""
from __future__ import annotations

H, OK, D, X = "hero", "ok", "detail", "offmodel"

CHARACTERS: dict[str, dict] = {
    "danny": {
        "title": "Danny Boice (Dad)",
        "descriptor": (
            "Completely bald shaved head; very long chest-length full beard (published tone ranges "
            "dark brown -> auburn/ginger -> sun-bleached blond-brown); heavy neck, forearm and chest "
            "tattoos (ornamental/floral sleeves); big athletic build; plain dark t-shirt and jeans "
            "(period garments go OVER the tee); tired, steady, deep-set eyes."),
        "trigger": "CHARACTERDADDANNY23",
        "panels": [
            (1, 74, H, "journal at desk, lamp - the 'last panel' template"),
            (1, 5, H, "release processing, standing, tee + jeans"),
            (1, 10, H, "seated on couch, forearms/hands clasped"),
            (1, 11, OK, "driving at dusk, profile"),
            (1, 14, H, "walking off bus, full figure"),
            (1, 71, H, "armchair, relaxed, forearm tattoos"),
            (1, 18, OK, "at window watching, profile"),
            (1, 22, OK, "eating at table, framed portrait behind"),
            (1, 63, OK, "period shirt, hand over face (embarrassed)"),
            (1, 40, X, "on horse in Rough Rider uniform; beard reads grey/pale - drift"),
            (1, 45, OK, "battle, pistol raised, period shirt"),
            (1, 46, OK, "battle, saber, forearm tattoos"),
            (1, 60, OK, "helping Teddy up"),
            (1, 33, OK, "landing in Cuba, crawling, uniform"),
            (1, 35, OK, "with Daniel in Cuba, uniform"),
            (1, 1, OK, "prison bunk, tank top, full tattoos"),
            (1, 3, OK, "prison, shirtless seated"),
            (1, 6, OK, "doorway, black tee, carrying box"),
            (1, 7, OK, "outside prison fence holding box"),
            (1, 50, H, "SHU, cross-legged, orange pants, full torso tattoos"),
            (1, 13, D, "rear view driving away, neck tattoos"),
            (1, 44, D, "back of head with Teddy"),
            (1, 8, D, "tattooed hand holding cash + bus ticket"),
            (1, 16, D, "ankle monitor and boot"),
            (2, 1, H, "couch, hands clasped, tattoos, wristwatch"),
            (2, 2, OK, "supervision-office armchair, side profile, skull tattoo"),
            (2, 3, X, "bib overalls at work job; costume-justified"),
            (2, 4, H, "grocery aisle, tee + jeans"),
            (2, 6, OK, "armchair, phone"),
            (2, 8, OK, "kitchen, phone, donut box on counter"),
            (2, 10, OK, "greeting Jen on sidewalk"),
            (2, 14, H, "doorway, full figure, tee + jeans"),
            (2, 20, OK, "radiating glow as the 'note' arrives"),
            (2, 29, X, "Brooklyn disguise: blue Champion sweatshirt - story-justified"),
            (2, 34, D, "back of head, with Cash and Daniel"),
            (2, 48, X, "flashback: suit, pre-prison executive life - NOT current canon look"),
        ],
    },
    "daniel": {
        "title": "Daniel 'The Bull' Boice (Son, 11)",
        "descriptor": (
            "Tall lean athletic 11-year-old; messy brown hair, tousled and slightly long on top; "
            "expressive dark eyes; typically a gray/olive hoodie in the present day; brown-belt "
            "Tae Kwon Do gi when training; always fully clothed. Quiet, intense stillness is his "
            "'tell'; mischief when eating donuts."),
        "trigger": "CHARACTERDANIELBULL23",
        "panels": [
            (1, 20, H, "driveway, smiling, hoodie, hands in pockets"),
            (1, 24, H, "eating, grinning"),
            (1, 26, H, "donut mid-bite on white"),
            (1, 36, H, "Cuba, period uniform, serious portrait"),
            (1, 59, H, "close portrait, cap, dirt"),
            (1, 72, H, "couch, hoodie + shorts, pensive"),
            (1, 19, OK, "getting out of the Jeep, backpack"),
            (1, 23, OK, "eating, hoodie"),
            (1, 27, OK, "sick-green after donut"),
            (1, 30, OK, "standing in the rift, silhouette"),
            (1, 34, OK, "lying in Cuba"),
            (1, 35, OK, "with Danny in Cuba"),
            (1, 41, OK, "riding horse, period uniform"),
            (1, 47, OK, "hiding in foliage, wide-brim hat"),
            (1, 54, OK, "flying tackle to save Teddy"),
            (1, 55, OK, "mid-air, debris"),
            (1, 56, OK, "lying in dirt, hat"),
            (1, 62, OK, "holding toilet-paper 'fax'"),
            (1, 68, OK, "holding shell casing souvenir, hat"),
            (1, 69, OK, "on horse eating donut"),
            (1, 9, X, "much younger Daniel asleep before a TV (Moana), flashback"),
            (1, 58, D, "back view with Teddy"),
            (1, 70, D, "back view at window with plant, black tee"),
            (1, 73, OK, "asleep in bed, hat flying"),
            (2, 5, H, "on phone, hoodie, couch"),
            (2, 7, H, "brown-belt gi, training"),
            (2, 17, OK, "setting up camera rig, hoodie"),
            (2, 18, OK, "eating donut to camera"),
            (2, 19, OK, "writing in notebook, donut"),
            (2, 21, OK, "eating donuts with drink"),
            (2, 23, H, "glowing close-up, fire-light"),
            (2, 30, H, "Brooklyn: Starter jacket, Raiders cap, chain, full figure"),
            (2, 38, OK, "serving food at block party, Raiders cap"),
            (2, 54, H, "smiling close-up, Raiders cap, gold chain"),
            (2, 55, X, "flashback: Daniel at prison visiting-room bench (age ~6-8)"),
            (2, 12, D, "back view walking to door, backpack"),
            (2, 34, D, "back of cap, with Danny and Cash"),
        ],
    },
    "grandpa": {
        "title": "Grandpa (Danny's father)",
        "descriptor": (
            "Older man, lean; swept-back brown-gray hair, short graying beard, wire-rim glasses, "
            "dark work jacket. Appears driving his truck. Canon: minimal; says little, pats shoulders. "
            "Only ONE published panel - a reference render set is needed."),
        "trigger": None,
        "panels": [
            (1, 15, H, "driving the truck at the prison lot, glasses, graying beard"),
            (1, 22, D, "framed portrait on dining-room wall behind Danny (unconfirmed who it depicts)"),
        ],
    },
    "jen": {
        "title": "Jen (Daniel's mom)",
        "descriptor": (
            "Early 40s; long straight black/dark hair worn loose; slim athletic, fitted dark top and "
            "leggings; composed, warm; taps her foot when worried. Drives Jeep (S1) / blue Audi A7 (S2). "
            "Only ONE published panel shows her - a reference render set is needed."),
        "trigger": None,
        "panels": [
            (2, 10, H, "on the sidewalk with Danny, profile"),
            (1, 17, D, "silhouettes in the green Jeep"),
        ],
    },
    "johnny_cash": {
        "title": "Johnny Cash (the holographic guide)",
        "descriptor": (
            "Always in black: long black frock coat, black shirt; dark swept-back pompadour; deeply "
            "lined face; glowing amber/white edge-light or halo - a hologram only Danny and Daniel see. "
            "Dry, warm, elliptical; vanishes before the right question can be asked."),
        "trigger": None,
        "panels": [
            (1, 37, H, "full-figure hologram with cyan edge-glow over the battlefield"),
            (1, 38, OK, "mid-air, pointing the way"),
            (2, 32, H, "radiant halo, arms open, 'Johnny Cash: The Man in Black' sign"),
            (2, 34, H, "close, over Danny's shoulder, direct stare"),
            (2, 36, OK, "waving goodbye, dissolving, guitar case on the road"),
        ],
    },
    "old_timer": {
        "title": "The Old-Timer (mysterious blind old man)",
        "descriptor": (
            "Ancient, long and weathered; MILK-WHITE clouded eyes; white/gray beard, gray swept hair; "
            "wears each era's costume 'like something that happened to him'. Recurs in every story, "
            "drops quantum-physics / Sacred Flame hints. The white eyes are the identifying constant."),
        "trigger": None,
        "panels": [
            (1, 64, H, "Rough Rider costume, white eyes, beard"),
            (2, 43, H, "cosmic star-chart backdrop, glowing white eyes, gray beard"),
            (2, 42, OK, "1992 Brooklyn: playing dominoes, white goatee (candidate - eyes not milk-white here)"),
        ],
    },
    "teddy_roosevelt": {
        "title": "Teddy Roosevelt (historical)",
        "descriptor": (
            "Round wire-rim pince-nez glasses, large mustache, wide-brim Rough Rider hat, polka-dot "
            "blue neckerchief, bandolier, khaki officer's uniform, saber. Public historical figure; "
            "keep the Mignola register."),
        "trigger": None,
        "panels": [
            (1, 61, H, "tight portrait"),
            (1, 44, H, "grinning beside Danny's shoulder, yellow neckerchief"),
            (1, 51, OK, "mounted, bandolier"),
            (1, 52, OK, "charging, bloody saber"),
            (1, 42, OK, "leading Rough Riders under the flag"),
            (1, 43, OK, "mounted charge, saber on shoulder"),
            (1, 57, OK, "on the ground, rifle"),
            (1, 58, OK, "speaking to Daniel"),
            (1, 60, OK, "being helped up by Danny"),
            (1, 67, OK, "walking away, saluting the sunrise"),
        ],
    },
    "biggie": {
        "title": "Biggie Smalls / The Notorious B.I.G. (historical)",
        "descriptor": (
            "Large frame; multicolor Coogi-style sweaters; heavy gold chain/medallion; fedora or Kangol "
            "variants and sunglasses; microphone on a Bed-Stuy stoop. Public historical figure depicted in "
            "Brooklyn, July 1992."),
        "trigger": None,
        "panels": [
            (2, 40, H, "rapping into mic, Coogi sweater"),
            (2, 41, OK, "leaning at the rail, paper bag"),
            (2, 51, H, "close-up with gold chain, patterned sweater"),
            (2, 53, OK, "sunglasses, mic, crowd"),
            (2, 33, OK, "eating, maroon jacket, Bed-Stuy banner"),
            (2, 56, OK, "holding 'Brooklyn's Finest MCs' bag"),
        ],
    },
    "prosecutor": {
        "title": "The Prosecutor (Director of the Fun Police)",
        "descriptor": (
            "Age 52; tall thin; long pointy face; slicked-back dark hair; ill-fitting charcoal pinstripe "
            "suit, red tie, pocket square; knockoff gold watch; cheap shiny shoes; vain, hollow. "
            "'Dude, you have no idea.'"),
        "trigger": "CHARACTERPROSECUTOR",
        "panels": [
            (2, 44, H, "full-figure model sheet with title banner"),
            (2, 45, H, "bust, red background, pinstripe + red tie"),
            (1, 48, OK, "Cuba: fedora, clipboard, pinstripe, badge"),
        ],
    },
    "hater": {
        "title": "The Hater (Fun Police)",
        "descriptor": (
            "Age 35; short, portly, round fleshy face, heavy jowls, lazy eye, acne, buck teeth; lank "
            "dark hair; navy Fun Police uniform with FBOP shield; untucked, straining shirt; 'No fun allowed!'"),
        "trigger": "CHARACTERHATER",
        "panels": [
            (2, 46, H, "full-figure model sheet"),
            (2, 47, H, "close portrait, scowl"),
            (1, 49, OK, "Cuba: campaign hat, uniform bust"),
        ],
    },
}

PLACES_OBJECTS: dict[str, dict] = {
    "grandpas_house_interior": {
        "title": "Grandpa's House - Interior",
        "kind": "place",
        "descriptor": "Warm amber-lit lived-in rooms: leather couch/armchairs, wood dining table, kitchen with window, framed photos, Danny's home-detention base.",
        "panels": [(1, 22, H, "dining room"), (1, 23, OK, "table"), (1, 24, OK, "table/kitchen"),
                   (1, 18, OK, "front window"), (1, 70, OK, "kitchen window + plant"), (1, 71, OK, "armchair"),
                   (1, 72, OK, "armchair"), (2, 1, OK, "couch"), (2, 6, OK, "armchair"), (2, 8, OK, "kitchen"),
                   (2, 14, OK, "doorway"), (2, 17, OK, "Daniel's camera nook"), (2, 18, OK, "kitchen table"),
                   (2, 19, OK, "kitchen table"), (2, 21, OK, "table")],
    },
    "grandpas_house_exterior": {
        "title": "Grandpa's House - Exterior",
        "kind": "place",
        "descriptor": "Two-story suburban home, wood siding, covered porch, driveway, mature trees; autumn oak; the blue Audi / green Jeep park out front.",
        "panels": [(2, 9, H, "street view with Audi"), (2, 11, H, "street view dusk"), (2, 12, OK, "orange front door"),
                   (1, 18, OK, "autumn tree through window"), (1, 20, OK, "driveway (Jen/Daniel street)"),
                   (1, 12, OK, "Jen's house at night (Danny's drive-by)")],
    },
    "space_time_continuum": {
        "title": "The Space-Time Continuum (the Crack)",
        "kind": "place",
        "descriptor": "A flaming vertical fissure splitting dark rock walls, stars and clock-faces swirling beyond; orange/ochre light bursting from the seam; cracked-pavement version on landing.",
        "panels": [(1, 29, H, "fiery fissure with tiny figure"), (1, 30, H, "Daniel in the rift"),
                   (1, 65, H, "spiral of clocks, grids, planets"), (2, 24, H, "lightning rift with hooded figures and flame"),
                   (2, 27, OK, "cracked Brooklyn pavement, pressure waves")],
    },
    "sacred_eternal_flame": {
        "title": "The Sacred Eternal Flame",
        "kind": "object",
        "descriptor": "A tall amber-orange tongue of fire in a ring of standing stones, tended by a circle of black-hooded figures with arms extended; starfield above.",
        "panels": [(1, 66, H, "ring of hooded keepers, standing stones"), (2, 24, H, "flame spiraling in the rift, hooded keepers")],
    },
    "fart_and_shockwaves": {
        "title": "The Fart / Shockwave registers",
        "kind": "object",
        "descriptor": "Each story invents its own visual register (S1 nuclear mushroom cloud; S2 concentric bass-wave rings and a trembling plant). Never repeat a prior register.",
        "panels": [(1, 28, H, "S1 mushroom cloud over a house"), (2, 20, H, "S2 radiating note"), (2, 22, H, "S2 plant in bass-wave rings"),
                   (2, 23, OK, "S2 Daniel in the burst")],
    },
    "entenmanns_donuts": {
        "title": "Entenmann's Chocolate Donuts (recurring object)",
        "kind": "object",
        "descriptor": "White/red Entenmann's box with script logo; glossy chocolate-glazed donuts; always the trigger.",
        "panels": [(1, 25, H, "box on counter"), (1, 31, H, "singed donuts after the return"), (1, 39, OK, "donuts in a 1st U.S. Cav haversack"),
                   (1, 26, OK, "mid-bite"), (2, 13, OK, "box + notebook + phone"), (2, 35, H, "donuts spilling from a red bag, Brooklyn 1992")],
    },
    "journals": {
        "title": "Danny's Journals",
        "kind": "object",
        "descriptor": "Black leather-bound journals with red ribbon; shelf of volumes; written under a single desk lamp - the story's frame.",
        "panels": [(1, 4, H, "journal shelf in the cell"), (1, 74, H, "writing at the desk")],
    },
    "donut_experiments_notebook": {
        "title": "Daniel's DONUT EXPERIMENTS notebook",
        "kind": "object",
        "descriptor": "Spiral notebook, marker lettering: DONUT EXPERIMENTS, VOL. 1 - confidential; hypothesis table, variable lists; phone-on-tripod camera rig.",
        "panels": [(2, 13, H, "cover"), (2, 15, H, "hypothesis page"), (2, 16, H, "variables page"), (2, 19, OK, "in use")],
    },
    "the_plant": {
        "title": "The Plant (Daniel talks to it)",
        "kind": "object",
        "descriptor": "A potted leafy plant on the window sill; Daniel's confidant; braces during the fart.",
        "panels": [(1, 70, H, "Daniel returning it to the sill"), (2, 22, H, "bracing in bass-wave rings")],
    },
    "vehicles": {
        "title": "Vehicles (Jen's Jeep, Audi, Grandpa's truck)",
        "kind": "object",
        "descriptor": "Jen's army-green Jeep Wrangler (S1); Jen's blue Audi A7 (S2 - continuity flag); Grandpa's older pickup.",
        "panels": [(1, 17, H, "green Jeep"), (1, 21, OK, "Jeep rear"), (1, 20, OK, "Jeep behind Daniel"),
                   (2, 9, H, "blue Audi A7"), (2, 11, OK, "Audi rear"), (1, 15, OK, "Grandpa's truck cab")],
    },
    "prison": {
        "title": "Prison (flashback environment)",
        "kind": "place",
        "descriptor": "Orange/amber light on black; barred windows; bunks; razor-wire; the SHU; visiting-room bolted tables. Danny in tank top / orange pants.",
        "panels": [(1, 1, OK, "bunk, waiting for count"), (1, 2, OK, "CO with flashlight"), (1, 3, OK, "waking after count"),
                   (1, 5, OK, "processing"), (1, 7, OK, "leaving"), (1, 50, H, "SHU"), (2, 55, H, "visiting room, Daniel on bench")],
    },
    "cuba_1898": {
        "title": "Cuba, July 1 1898 (Story 1 setting)",
        "kind": "place",
        "descriptor": "Red-ochre dust, palms, fence lines and trenches; Rough Riders under the Stars and Stripes; smoke columns and exploding shells.",
        "panels": [(1, 32, H, "wide trench/hill"), (1, 33, OK, "landing"), (1, 42, H, "Rough Riders assemble"),
                   (1, 52, OK, "battle"), (1, 53, OK, "sniper in palms"), (1, 67, OK, "sunrise salute")],
    },
    "brooklyn_1992": {
        "title": "Bedford-Stuyvesant, Brooklyn, July 1992 (Story 2 setting)",
        "kind": "place",
        "descriptor": "Brick brownstones, fire escapes, open hydrant with rainbow, DJ turntables, speaker stacks, BBQ grills, domino tables, bunting, Bed-Stuy Summer Jam banners; gold-hour haze.",
        "panels": [(2, 25, H, "block party wide"), (2, 26, H, "hydrant rainbow"), (2, 28, OK, "fire escape + boombox"),
                   (2, 31, H, "block party street"), (2, 37, OK, "food + DJ"), (2, 52, OK, "DJ at Summer Jam"),
                   (2, 39, OK, "the corner")],
    },
}

SOUVENIRS = [(1, 68, "Spent shell casing (Story 1)")]
