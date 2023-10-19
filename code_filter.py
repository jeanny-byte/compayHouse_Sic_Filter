import pandas as pd
from tqdm import tqdm  # Import tqdm for progress bar

# Create a dictionary mapping SIC codes to human-readable names
sic_code_to_name = {
    9100 : "Support activities for petroleum and natural gas mining",
9900 : "Support activities for other mining and quarrying",
10110 : "Processing and preserving of meat",
10120 : "Processing and preserving of poultry meat",
10130 : "Production of meat and poultry meat products",
10200 : "Processing and preserving of fish, crustaceans and molluscs",
10310 : "Processing and preserving of potatoes",
10320 : "Manufacture of fruit and vegetable juice",
10390 : "Other processing and preserving of fruit and vegetables",
10410 : "Manufacture of oils and fats",
10420 : "Manufacture of margarine and similar edible fats",
10511 : "Liquid milk and cream production",
10512 : "Butter and cheese production",
10519 : "Manufacture of other milk products",
10520 : "Manufacture of ice cream",
10611 : "Grain milling",
10612 : "Manufacture of breakfast cereals and cereals-based food",
10620 : "Manufacture of starches and starch products",
10710 : "Manufacture of bread; manufacture of fresh pastry goods and cakes",
10720 : "Manufacture of rusks and biscuits; manufacture of preserved pastry goods and cakes",
10730 : "Manufacture of macaroni, noodles, couscous and similar farinaceous products",
10810 : "Manufacture of sugar",
10821 : "Manufacture of cocoa and chocolate confectionery",
10822 : "Manufacture of sugar confectionery",
10831 : "Tea processing",
10832 : "Production of coffee and coffee substitutes",
10840 : "Manufacture of condiments and seasonings",
10850 : "Manufacture of prepared meals and dishes",
10860 : "Manufacture of homogenized food preparations and dietetic food",
10890 : "Manufacture of other food products n.e.c.",
10910 : "Manufacture of prepared feeds for farm animals",
10920 : "Manufacture of prepared pet foods",
11010 : "Distilling, rectifying and blending of spirits",
11020 : "Manufacture of wine from grape",
11030 : "Manufacture of cider and other fruit wines",
11040 : "Manufacture of other non-distilled fermented beverages",
11050 : "Manufacture of beer",
11060 : "Manufacture of malt",
11070 : "Manufacture of soft drinks; production of mineral waters and other bottled waters",
12000 : "Manufacture of tobacco products",
13100 : "Preparation and spinning of textile fibres",
13200 : "Weaving of textiles",
13300 : "Finishing of textiles",
13910 : "Manufacture of knitted and crocheted fabrics",
13921 : "Manufacture of soft furnishings",
13922 : "manufacture of canvas goods, sacks, etc.",
13923 : "manufacture of household textiles",
13931 : "Manufacture of woven or tufted carpets and rugs",
13939 : "Manufacture of other carpets and rugs",
13940 : "Manufacture of cordage, rope, twine and netting",
13950 : "Manufacture of non-wovens and articles made from non-wovens, except apparel",
13960 : "Manufacture of other technical and industrial textiles",
13990 : "Manufacture of other textiles n.e.c.",
14110 : "Manufacture of leather clothes",
14120 : "Manufacture of workwear",
14131 : "Manufacture of other men's outerwear",
14132 : "Manufacture of other women's outerwear",
14141 : "Manufacture of men's underwear",
14142 : "Manufacture of women's underwear",
14190 : "Manufacture of other wearing apparel and accessories n.e.c.",
14200 : "Manufacture of articles of fur",
14310 : "Manufacture of knitted and crocheted hosiery",
14390 : "Manufacture of other knitted and crocheted apparel",
15110 : "Tanning and dressing of leather; dressing and dyeing of fur",
15120 : "Manufacture of luggage, handbags and the like, saddlery and harness",
15200 : "Manufacture of footwear",
16100 : "Sawmilling and planing of wood",
16210 : "Manufacture of veneer sheets and wood-based panels",
16220 : "Manufacture of assembled parquet floors",
16230 : "Manufacture of other builders' carpentry and joinery",
16240 : "Manufacture of wooden containers",
16290 : "Manufacture of other products of wood; manufacture of articles of cork, straw and plaiting materials",
17110 : "Manufacture of pulp",
17120 : "Manufacture of paper and paperboard",
17211 : "Manufacture of corrugated paper and paperboard, sacks and bags",
17219 : "Manufacture of other paper and paperboard containers",
17220 : "Manufacture of household and sanitary goods and of toilet requisites",
17230 : "Manufacture of paper stationery",
17240 : "Manufacture of wallpaper",
17290 : "Manufacture of other articles of paper and paperboard n.e.c.",
18110 : "Printing of newspapers",
18121 : "Manufacture of printed labels",
18129 : "Printing n.e.c.",
18130 : "Pre-press and pre-media services",
18140 : "Binding and related services",
18201 : "Reproduction of sound recording",
18202 : "Reproduction of video recording",
18203 : "Reproduction of computer media",
19100 : "Manufacture of coke oven products",
19201 : "Mineral oil refining",
19209 : "Other treatment of petroleum products (excluding petrochemicals manufacture)",
20110 : "Manufacture of industrial gases",
20120 : "Manufacture of dyes and pigments",
20130 : "Manufacture of other inorganic basic chemicals",
20140 : "Manufacture of other organic basic chemicals",
20150 : "Manufacture of fertilizers and nitrogen compounds",
20160 : "Manufacture of plastics in primary forms",
20170 : "Manufacture of synthetic rubber in primary forms",
20200 : "Manufacture of pesticides and other agrochemical products",
20301 : "Manufacture of paints, varnishes and similar coatings, mastics and sealants",
20302 : "Manufacture of printing ink",
20411 : "Manufacture of soap and detergents",
20412 : "Manufacture of cleaning and polishing preparations",
20420 : "Manufacture of perfumes and toilet preparations",
20510 : "Manufacture of explosives",
20520 : "Manufacture of glues",
20530 : "Manufacture of essential oils",
20590 : "Manufacture of other chemical products n.e.c.",
20600 : "Manufacture of man-made fibres",
21100 : "Manufacture of basic pharmaceutical products",
21200 : "Manufacture of pharmaceutical preparations",
22110 : "Manufacture of rubber tyres and tubes; retreading and rebuilding of rubber tyres",
22190 : "Manufacture of other rubber products",
22210 : "Manufacture of plastic plates, sheets, tubes and profiles",
22220 : "Manufacture of plastic packing goods",
22230 : "Manufacture of builders ware of plastic",
22290 : "Manufacture of other plastic products",
23110 : "Manufacture of flat glass",
23120 : "Shaping and processing of flat glass",
23130 : "Manufacture of hollow glass",
23140 : "Manufacture of glass fibres",
23190 : "Manufacture and processing of other glass, including technical glassware",
23200 : "Manufacture of refractory products",
23310 : "Manufacture of ceramic tiles and flags",
23320 : "Manufacture of bricks, tiles and construction products, in baked clay",
23410 : "Manufacture of ceramic household and ornamental articles",
23420 : "Manufacture of ceramic sanitary fixtures",
23430 : "Manufacture of ceramic insulators and insulating fittings",
23440 : "Manufacture of other technical ceramic products",
23490 : "Manufacture of other ceramic products n.e.c.",
23510 : "Manufacture of cement",
23520 : "Manufacture of lime and plaster",
23610 : "Manufacture of concrete products for construction purposes",
23620 : "Manufacture of plaster products for construction purposes",
23630 : "Manufacture of ready-mixed concrete",
23640 : "Manufacture of mortars",
23650 : "Manufacture of fibre cement",
23690 : "Manufacture of other articles of concrete, plaster and cement",
23700 : "Cutting, shaping and finishing of stone",
23910 : "Production of abrasive products",
23990 : "Manufacture of other non-metallic mineral products n.e.c.",
24100 : "Manufacture of basic iron and steel and of ferro-alloys",
24200 : "Manufacture of tubes, pipes, hollow profiles and related fittings, of steel",
24310 : "Cold drawing of bars",
24320 : "Cold rolling of narrow strip",
24330 : "Cold forming or folding",
24340 : "Cold drawing of wire",
24410 : "Precious metals production",
24420 : "Aluminium production",
24430 : "Lead, zinc and tin production",
24440 : "Copper production",
24450 : "Other non-ferrous metal production",
24460 : "Processing of nuclear fuel",
24510 : "Casting of iron",
24520 : "Casting of steel",
24530 : "Casting of light metals",
24540 : "Casting of other non-ferrous metals",
25110 : "Manufacture of metal structures and parts of structures",
25120 : "Manufacture of doors and windows of metal",
25210 : "Manufacture of central heating radiators and boilers",
25290 : "Manufacture of other tanks, reservoirs and containers of metal",
25300 : "Manufacture of steam generators, except central heating hot water boilers",
25400 : "Manufacture of weapons and ammunition",
25500 : "Forging, pressing, stamping and roll-forming of metal; powder metallurgy",
25610 : "Treatment and coating of metals",
25620 : "Machining",
25710 : "Manufacture of cutlery",
25720 : "Manufacture of locks and hinges",
25730 : "Manufacture of tools",
25910 : "Manufacture of steel drums and similar containers",
25920 : "Manufacture of light metal packaging",
25930 : "Manufacture of wire products, chain and springs",
25940 : "Manufacture of fasteners and screw machine products",
25990 : "Manufacture of other fabricated metal products n.e.c.",
26110 : "Manufacture of electronic components",
26120 : "Manufacture of loaded electronic boards",
26200 : "Manufacture of computers and peripheral equipment",
26301 : "Manufacture of telegraph and telephone apparatus and equipment",
26309 : "Manufacture of communication equipment other than telegraph, and telephone apparatus and equipment",
26400 : "Manufacture of consumer electronics",
26511 : "Manufacture of electronic measuring, testing etc. equipment, not for industrial process control",
26512 : "Manufacture of electronic industrial process control equipment",
26513 : "Manufacture of non-electronic measuring, testing etc. equipment, not for industrial process control",
26514 : "Manufacture of non-electronic industrial process control equipment",
26520 : "Manufacture of watches and clocks",
26600 : "Manufacture of irradiation, electromedical and electrotherapeutic equipment",
26701 : "Manufacture of optical precision instruments",
26702 : "Manufacture of photographic and cinematographic equipment",
26800 : "Manufacture of magnetic and optical media",
27110 : "Manufacture of electric motors, generators and transformers",
27120 : "Manufacture of electricity distribution and control apparatus",
27200 : "Manufacture of batteries and accumulators",
27310 : "Manufacture of fibre optic cables",
27320 : "Manufacture of other electronic and electric wires and cables",
27330 : "Manufacture of wiring devices",
27400 : "Manufacture of electric lighting equipment",
27510 : "Manufacture of electric domestic appliances",
27520 : "Manufacture of non-electric domestic appliances",
27900 : "Manufacture of other electrical equipment",
28110 : "Manufacture of engines and turbines, except aircraft, vehicle and cycle engines",
28120 : "Manufacture of fluid power equipment",
28131 : "Manufacture of pumps",
28132 : "Manufacture of compressors",
28140 : "Manufacture of taps and valves",
28150 : "Manufacture of bearings, gears, gearing and driving elements",
28210 : "Manufacture of ovens, furnaces and furnace burners",
28220 : "Manufacture of lifting and handling equipment",
28230 : "Manufacture of office machinery and equipment (except computers and peripheral equipment)",
28240 : "Manufacture of power-driven hand tools",
28250 : "Manufacture of non-domestic cooling and ventilation equipment",
28290 : "Manufacture of other general-purpose machinery n.e.c.",
28301 : "Manufacture of agricultural tractors",
28302 : "Manufacture of agricultural and forestry machinery other than tractors",
28410 : "Manufacture of metal forming machinery",
28490 : "Manufacture of other machine tools",
28910 : "Manufacture of machinery for metallurgy",
28921 : "Manufacture of machinery for mining",
28922 : "Manufacture of earthmoving equipment",
28923 : "Manufacture of equipment for concrete crushing and screening and roadworks",
28930 : "Manufacture of machinery for food, beverage and tobacco processing",
28940 : "Manufacture of machinery for textile, apparel and leather production",
28950 : "Manufacture of machinery for paper and paperboard production",
28960 : "Manufacture of plastics and rubber machinery",
28990 : "Manufacture of other special-purpose machinery n.e.c.",
29100 : "Manufacture of motor vehicles",
29201 : "Manufacture of bodies (coachwork) for motor vehicles (except caravans)",
29202 : "Manufacture of trailers and semi-trailers",
29203 : "Manufacture of caravans",
29310 : "Manufacture of electrical and electronic equipment for motor vehicles and their engines",
29320 : "Manufacture of other parts and accessories for motor vehicles",
30110 : "Building of ships and floating structures",
30120 : "Building of pleasure and sporting boats",
30200 : "Manufacture of railway locomotives and rolling stock",
30300 : "Manufacture of air and spacecraft and related machinery",
30400 : "Manufacture of military fighting vehicles",
30910 : "Manufacture of motorcycles",
30920 : "Manufacture of bicycles and invalid carriages",
30990 : "Manufacture of other transport equipment n.e.c.",
31010 : "Manufacture of office and shop furniture",
31020 : "Manufacture of kitchen furniture",
31030 : "Manufacture of mattresses",
31090 : "Manufacture of other furniture",
32110 : "Striking of coins",
32120 : "Manufacture of jewellery and related articles",
32130 : "Manufacture of imitation jewellery and related articles",
32200 : "Manufacture of musical instruments",
32300 : "Manufacture of sports goods",
32401 : "Manufacture of professional and arcade games and toys",
32409 : "Manufacture of other games and toys, n.e.c.",
32500 : "Manufacture of medical and dental instruments and supplies",
32910 : "Manufacture of brooms and brushes",
32990 : "Other manufacturing n.e.c.",
33110 : "Repair of fabricated metal products",
33120 : "Repair of machinery",
33130 : "Repair of electronic and optical equipment",
33140 : "Repair of electrical equipment",
33150 : "Repair and maintenance of ships and boats",
33160 : "Repair and maintenance of aircraft and spacecraft",
33170 : "Repair and maintenance of other transport equipment n.e.c.",
33190 : "Repair of other equipment",
33200 : "Installation of industrial machinery and equipment",
35110 : "Production of electricity",
35120 : "Transmission of electricity",
35130 : "Distribution of electricity",
35140 : "Trade of electricity",
35210 : "Manufacture of gas",
35220 : "Distribution of gaseous fuels through mains",
35230 : "Trade of gas through mains",
35300 : "Steam and air conditioning supply",
36000 : "Water collection, treatment and supply",
37000 : "Sewerage",
38110 : "Collection of non-hazardous waste",
38120 : "Collection of hazardous waste",
38210 : "Treatment and disposal of non-hazardous waste",
38220 : "Treatment and disposal of hazardous waste",
38310 : "Dismantling of wrecks",
38320 : "Recovery of sorted materials",
39000 : "Remediation activities and other waste management services",
41100 : "Development of building projects",
41201 : "Construction of commercial buildings",
41202 : "Construction of domestic buildings",
42110 : "Construction of roads and motorways",
42120 : "Construction of railways and underground railways",
42130 : "Construction of bridges and tunnels",
42210 : "Construction of utility projects for fluids",
42220 : "Construction of utility projects for electricity and telecommunications",
42910 : "Construction of water projects",
42990 : "Construction of other civil engineering projects n.e.c.",
43110 : "Demolition",
43120 : "Site preparation",
43130 : "Test drilling and boring",
43210 : "Electrical installation",
43220 : "Plumbing, heat and air-conditioning installation",
43290 : "Other construction installation",
43310 : "Plastering",
43320 : "Joinery installation",
43330 : "Floor and wall covering",
43341 : "Painting",
43342 : "Glazing",
43390 : "Other building completion and finishing",
43910 : "Roofing activities",
43991 : "Scaffold erection",
43999 : "Other specialised construction activities n.e.c.",
45111 : "Sale of new cars and light motor vehicles",
45112 : "Sale of used cars and light motor vehicles",
45190 : "Sale of other motor vehicles",
45200 : "Maintenance and repair of motor vehicles",
45310 : "Wholesale trade of motor vehicle parts and accessories",
45320 : "Retail trade of motor vehicle parts and accessories",
45400 : "Sale, maintenance and repair of motorcycles and related parts and accessories",
46110 : "Agents selling agricultural raw materials, livestock, textile raw materials and semi-finished goods",
46120 : "Agents involved in the sale of fuels, ores, metals and industrial chemicals",
46130 : "Agents involved in the sale of timber and building materials",
46140 : "Agents involved in the sale of machinery, industrial equipment, ships and aircraft",
46150 : "Agents involved in the sale of furniture, household goods, hardware and ironmongery",
46160 : "Agents involved in the sale of textiles, clothing, fur, footwear and leather goods",
46170 : "Agents involved in the sale of food, beverages and tobacco",
46180 : "Agents specialised in the sale of other particular products",
46190 : "Agents involved in the sale of a variety of goods",
46210 : "Wholesale of grain, unmanufactured tobacco, seeds and animal feeds",
46220 : "Wholesale of flowers and plants",
46230 : "Wholesale of live animals",
46240 : "Wholesale of hides, skins and leather",
46310 : "Wholesale of fruit and vegetables",
46320 : "Wholesale of meat and meat products",
46330 : "Wholesale of dairy products, eggs and edible oils and fats",
46341 : "Wholesale of fruit and vegetable juices, mineral water and soft drinks",
46342 : "Wholesale of wine, beer, spirits and other alcoholic beverages",
46350 : "Wholesale of tobacco products",
46360 : "Wholesale of sugar and chocolate and sugar confectionery",
46370 : "Wholesale of coffee, tea, cocoa and spices",
46380 : "Wholesale of other food, including fish, crustaceans and molluscs",
46390 : "Non-specialised wholesale of food, beverages and tobacco",
46410 : "Wholesale of textiles",
46420 : "Wholesale of clothing and footwear",
46431 : "Wholesale of audio tapes, records, CDs and video tapes and the equipment on which these are played",
46439 : "Wholesale of radio, television goods & electrical household appliances (other than records, tapes, CD's & video tapes and the equipment used for playing them)",
46440 : "Wholesale of china and glassware and cleaning materials",
46450 : "Wholesale of perfume and cosmetics",
46460 : "Wholesale of pharmaceutical goods",
46470 : "Wholesale of furniture, carpets and lighting equipment",
46480 : "Wholesale of watches and jewellery",
46491 : "Wholesale of musical instruments",
46499 : "Wholesale of household goods (other than musical instruments) n.e.c",
46510 : "Wholesale of computers, computer peripheral equipment and software",
46520 : "Wholesale of electronic and telecommunications equipment and parts",
46610 : "Wholesale of agricultural machinery, equipment and supplies",
46620 : "Wholesale of machine tools",
46630 : "Wholesale of mining, construction and civil engineering machinery",
46640 : "Wholesale of machinery for the textile industry and of sewing and knitting machines",
46650 : "Wholesale of office furniture",
46660 : "Wholesale of other office machinery and equipment",
46690 : "Wholesale of other machinery and equipment",
46711 : "Wholesale of petroleum and petroleum products",
46719 : "Wholesale of other fuels and related products",
46720 : "Wholesale of metals and metal ores",
46730 : "Wholesale of wood, construction materials and sanitary equipment",
46740 : "Wholesale of hardware, plumbing and heating equipment and supplies",
46750 : "Wholesale of chemical products",
46760 : "Wholesale of other intermediate products",
46770 : "Wholesale of waste and scrap",
46900 : "Non-specialised wholesale trade",
47110 : "Retail sale in non-specialised stores with food, beverages or tobacco predominating",
47190 : "Other retail sale in non-specialised stores",
47210 : "Retail sale of fruit and vegetables in specialised stores",
47220 : "Retail sale of meat and meat products in specialised stores",
47230 : "Retail sale of fish, crustaceans and molluscs in specialised stores",
47240 : "Retail sale of bread, cakes, flour confectionery and sugar confectionery in specialised stores",
47250 : "Retail sale of beverages in specialised stores",
47260 : "Retail sale of tobacco products in specialised stores",
47290 : "Other retail sale of food in specialised stores",
47300 : "Retail sale of automotive fuel in specialised stores",
47410 : "Retail sale of computers, peripheral units and software in specialised stores",
47421 : "Retail sale of mobile telephones",
47429 : "Retail sale of telecommunications equipment other than mobile telephones",
47430 : "Retail sale of audio and video equipment in specialised stores",
47510 : "Retail sale of textiles in specialised stores",
47520 : "Retail sale of hardware, paints and glass in specialised stores",
47530 : "Retail sale of carpets, rugs, wall and floor coverings in specialised stores",
47540 : "Retail sale of electrical household appliances in specialised stores",
47591 : "Retail sale of musical instruments and scores",
47599 : "Retail of furniture, lighting, and similar (not musical instruments or scores) in specialised store",
47610 : "Retail sale of books in specialised stores",
47620 : "Retail sale of newspapers and stationery in specialised stores",
47630 : "Retail sale of music and video recordings in specialised stores",
47640 : "Retail sale of sports goods, fishing gear, camping goods, boats and bicycles",
47650 : "Retail sale of games and toys in specialised stores",
47710 : "Retail sale of clothing in specialised stores",
47721 : "Retail sale of footwear in specialised stores",
47722 : "Retail sale of leather goods in specialised stores",
47730 : "Dispensing chemist in specialised stores",
47741 : "Retail sale of hearing aids",
47749 : "Retail sale of medical and orthopaedic goods in specialised stores (not incl. hearing aids) n.e.c.",
47750 : "Retail sale of cosmetic and toilet articles in specialised stores",
47760 : "Retail sale of flowers, plants, seeds, fertilizers, pet animals and pet food in specialised stores",
47770 : "Retail sale of watches and jewellery in specialised stores",
47781 : "Retail sale in commercial art galleries",
47782 : "Retail sale by opticians",
47789 : "Other retail sale of new goods in specialised stores (not commercial art galleries and opticians)",
47791 : "Retail sale of antiques including antique books in stores",
47799 : "Retail sale of other second-hand goods in stores (not incl. antiques)",
47810 : "Retail sale via stalls and markets of food, beverages and tobacco products",
47820 : "Retail sale via stalls and markets of textiles, clothing and footwear",
47890 : "Retail sale via stalls and markets of other goods",
47910 : "Retail sale via mail order houses or via Internet",
47990 : "Other retail sale not in stores, stalls or markets",
49100 : "Passenger rail transport, interurban",
49200 : "Freight rail transport",
49311 : "Urban and suburban passenger railway transportation by underground, metro and similar systems",
49319 : "Other urban, suburban or metropolitan passenger land transport (not underground, metro or similar)",
49320 : "Taxi operation",
49390 : "Other passenger land transport",
49410 : "Freight transport by road",
49420 : "Removal services",
49500 : "Transport via pipeline",
50100 : "Sea and coastal passenger water transport",
50200 : "Sea and coastal freight water transport",
50300 : "Inland passenger water transport",
50400 : "Inland freight water transport",
51101 : "Scheduled passenger air transport",
51102 : "Non-scheduled passenger air transport",
51210 : "Freight air transport",
51220 : "Space transport",
52101 : "Operation of warehousing and storage facilities for water transport activities",
52102 : "Operation of warehousing and storage facilities for air transport activities",
52103 : "Operation of warehousing and storage facilities for land transport activities",
52211 : "Operation of rail freight terminals",
52212 : "Operation of rail passenger facilities at railway stations",
52213 : "Operation of bus and coach passenger facilities at bus and coach stations",
52219 : "Other service activities incidental to land transportation, n.e.c.",
52220 : "Service activities incidental to water transportation",
52230 : "Service activities incidental to air transportation",
52241 : "Cargo handling for water transport activities",
52242 : "Cargo handling for air transport activities",
52243 : "Cargo handling for land transport activities",
52290 : "Other transportation support activities",
53100 : "Postal activities under universal service obligation",
53201 : "Licensed carriers",
53202 : "Unlicensed carriers",
55100 : "Hotels and similar accommodation",
55201 : "Holiday centres and villages",
55202 : "Youth hostels",
55209 : "Other holiday and other collective accommodation",
55300 : "Recreational vehicle parks, trailer parks and camping grounds",
55900 : "Other accommodation",
56101 : "Licenced restaurants",
56102 : "Unlicenced restaurants and cafes",
56103 : "Take-away food shops and mobile food stands",
56210 : "Event catering activities",
56290 : "Other food services",
56301 : "Licenced clubs",
56302 : "Public houses and bars",
58110 : "Book publishing",
58120 : "Publishing of directories and mailing lists",
58130 : "Publishing of newspapers",
58141 : "Publishing of learned journals",
58142 : "Publishing of consumer and business journals and periodicals",
58190 : "Other publishing activities",
58210 : "Publishing of computer games",
58290 : "Other software publishing",
59111 : "Motion picture production activities",
59112 : "Video production activities",
59113 : "Television programme production activities",
59120 : "Motion picture, video and television programme post-production activities",
59131 : "Motion picture distribution activities",
59132 : "Video distribution activities",
59133 : "Television programme distribution activities",
59140 : "Motion picture projection activities",
59200 : "Sound recording and music publishing activities",
60100 : "Radio broadcasting",
60200 : "Television programming and broadcasting activities",
61100 : "Wired telecommunications activities",
61200 : "Wireless telecommunications activities",
61300 : "Satellite telecommunications activities",
61900 : "Other telecommunications activities",
62011 : "Ready-made interactive leisure and entertainment software development",
62012 : "Business and domestic software development",
62020 : "Information technology consultancy activities",
62030 : "Computer facilities management activities",
62090 : "Other information technology service activities",
63110 : "Data processing, hosting and related activities",
63120 : "Web portals",
63910 : "News agency activities",
63990 : "Other information service activities n.e.c.",
64110 : "Central banking",
64191 : "Banks",
64192 : "Building societies",
64201 : "Activities of agricultural holding companies",
64202 : "Activities of production holding companies",
64203 : "Activities of construction holding companies",
64204 : "Activities of distribution holding companies",
64205 : "Activities of financial services holding companies",
64209 : "Activities of other holding companies n.e.c.",
64301 : "Activities of investment trusts",
64302 : "Activities of unit trusts",
64303 : "Activities of venture and development capital companies",
64304 : "Activities of open-ended investment companies",
64305 : "Activities of property unit trusts",
64306 : "Activities of real estate investment trusts",
64910 : "Financial leasing",
64921 : "Credit granting by non-deposit taking finance houses and other specialist consumer credit grantors",
64922 : "Activities of mortgage finance companies",
64929 : "Other credit granting n.e.c.",
64991 : "Security dealing on own account",
64992 : "Factoring",
64999 : "Financial intermediation not elsewhere classified",
65110 : "Life insurance",
65120 : "Non-life insurance",
65201 : "Life reinsurance",
65202 : "Non-life reinsurance",
65300 : "Pension funding",
66110 : "Administration of financial markets",
66120 : "Security and commodity contracts dealing activities",
66190 : "Activities auxiliary to financial intermediation n.e.c.",
66210 : "Risk and damage evaluation",
66220 : "Activities of insurance agents and brokers",
66290 : "Other activities auxiliary to insurance and pension funding",
66300 : "Fund management activities",
68100 : "Buying and selling of own real estate",
68201 : "Renting and operating of Housing Association real estate",
68202 : "Letting and operating of conference and exhibition centres",
68209 : "Other letting and operating of own or leased real estate",
68310 : "Real estate agencies",
68320 : "Management of real estate on a fee or contract basis",
69101 : "Barristers at law",
69102 : "Solicitors",
69109 : "Activities of patent and copyright agents; other legal activities n.e.c.",
69201 : "Accounting and auditing activities",
69202 : "Bookkeeping activities",
69203 : "Tax consultancy",
70100 : "Activities of head offices",
70210 : "Public relations and communications activities",
70221 : "Financial management",
70229 : "Management consultancy activities other than financial management",
71111 : "Architectural activities",
71112 : "Urban planning and landscape architectural activities",
71121 : "Engineering design activities for industrial process and production",
71122 : "Engineering related scientific and technical consulting activities",
71129 : "Other engineering activities",
71200 : "Technical testing and analysis",
72110 : "Research and experimental development on biotechnology",
72190 : "Other research and experimental development on natural sciences and engineering",
72200 : "Research and experimental development on social sciences and humanities",
73110 : "Advertising agencies",
73120 : "Media representation services",
73200 : "Market research and public opinion polling",
74100 : "specialised design activities",
74201 : "Portrait photographic activities",
74202 : "Other specialist photography",
74203 : "Film processing",
74209 : "Photographic activities not elsewhere classified",
74300 : "Translation and interpretation activities",
74901 : "Environmental consulting activities",
74902 : "Quantity surveying activities",
74909 : "Other professional, scientific and technical activities n.e.c.",
74990 : "Non-trading company",
75000 : "Veterinary activities",
77110 : "Renting and leasing of cars and light motor vehicles",
77120 : "Renting and leasing of trucks and other heavy vehicles",
77210 : "Renting and leasing of recreational and sports goods",
77220 : "Renting of video tapes and disks",
77291 : "Renting and leasing of media entertainment equipment",
77299 : "Renting and leasing of other personal and household goods",
77310 : "Renting and leasing of agricultural machinery and equipment",
77320 : "Renting and leasing of construction and civil engineering machinery and equipment",
77330 : "Renting and leasing of office machinery and equipment (including computers)",
77341 : "Renting and leasing of passenger water transport equipment",
77342 : "Renting and leasing of freight water transport equipment",
77351 : "Renting and leasing of air passenger transport equipment",
77352 : "Renting and leasing of freight air transport equipment",
77390 : "Renting and leasing of other machinery, equipment and tangible goods n.e.c.",
77400 : "Leasing of intellectual property and similar products, except copyright works",
78101 : "Motion picture, television and other theatrical casting activities",
78109 : "Other activities of employment placement agencies",
78200 : "Temporary employment agency activities",
78300 : "Human resources provision and management of human resources functions",
79110 : "Travel agency activities",
79120 : "Tour operator activities",
79901 : "Activities of tourist guides",
79909 : "Other reservation service activities n.e.c.",
80100 : "Private security activities",
80200 : "Security systems service activities",
80300 : "Investigation activities",
81100 : "Combined facilities support activities",
81210 : "General cleaning of buildings",
81221 : "Window cleaning services",
81222 : "Specialised cleaning services",
81223 : "Furnace and chimney cleaning services",
81229 : "Other building and industrial cleaning activities",
81291 : "Disinfecting and exterminating services",
81299 : "Other cleaning services",
81300 : "Landscape service activities",
82110 : "Combined office administrative service activities",
82190 : "Photocopying, document preparation and other specialised office support activities",
82200 : "Activities of call centres",
82301 : "Activities of exhibition and fair organisers",
82302 : "Activities of conference organisers",
82911 : "Activities of collection agencies",
82912 : "Activities of credit bureaus",
82920 : "Packaging activities",
82990 : "Other business support service activities n.e.c.",
84110 : "General public administration activities",
84120 : "Regulation of health care, education, cultural and other social services, not incl. social security",
84130 : "Regulation of and contribution to more efficient operation of businesses",
84210 : "Foreign affairs",
84220 : "Defence activities",
84230 : "Justice and judicial activities",
84240 : "Public order and safety activities",
84250 : "Fire service activities",
84300 : "Compulsory social security activities",
85100 : "Pre-primary education",
85200 : "Primary education",
85310 : "General secondary education",
85320 : "Technical and vocational secondary education",
85410 : "Post-secondary non-tertiary education",
85421 : "First-degree level higher education",
85422 : "Post-graduate level higher education",
85510 : "Sports and recreation education",
85520 : "Cultural education",
85530 : "Driving school activities",
85590 : "Other education n.e.c.",
85600 : "Educational support services",
86101 : "Hospital activities",
86102 : "Medical nursing home activities",
86210 : "General medical practice activities",
86220 : "Specialists medical practice activities",
86230 : "Dental practice activities",
86900 : "Other human health activities",

    # Add more SIC codes and names as needed
}

# Modify the main_target_numbers to use SIC codes
main_target_numbers = list(sic_code_to_name.keys())

def process_csv(file_path, target_numbers, chunk_size=1000):
    """
    Process a CSV file, filter rows based on target numbers, and save the filtered data.

    Parameters:
        file_path (str): The path to the CSV file.
        target_numbers (list): List of target numbers (SIC codes) to filter rows.
        chunk_size (int, optional): The chunk size for reading the CSV file. Defaults to 1000.

    Returns:
        None
    """
    # Create a dictionary to store data for each target number
    target_data = {number: [] for number in target_numbers}
    processed_rows = 0  # Initialize a counter for processed rows

    # Calculate the total number of rows in the CSV file
    total_rows = sum(1 for _ in open(file_path))

    # Create a tqdm progress bar
    progress_bar = tqdm(total=total_rows, unit=" rows")

    # Read the CSV file in chunks and process each chunk
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        for _, row in chunk.iterrows():
            for col in ['SICCode.SicText_1', 'SICCode.SicText_2', 'SICCode.SicText_3', 'SICCode.SicText_4']:
                sic_code_str = str(row[col]).split('-')[0].strip()
                try:
                    sic_code = int(sic_code_str)
                    if sic_code in target_numbers:
                        target_data[sic_code].append(row)
                except ValueError:
                    pass
            processed_rows += 1
            progress_bar.update(1)  # Update the progress bar

    # Close the progress bar
    progress_bar.close()

    # Save the filtered data using SIC codes in the filename
    save_filtered_data(target_data, sic_code_to_name)


def save_filtered_data(target_data, sic_code_to_name):
    """
    Save the filtered data to separate CSV files with SIC codes in the filename.

    Parameters:
        target_data (dict): Dictionary containing the filtered data for each target number.
        sic_code_to_name (dict): Dictionary mapping SIC codes to human-readable names.

    Returns:
        None
    """
    for sic_code, rows in target_data.items():
        if len(target_data) == 1:
            # If only one SIC code was used, save the file as SIC_Code_Human-Readable-Name.csv
            name = sic_code_to_name.get(sic_code, f"SIC_Code_{sic_code}")
            filename = f"{sic_code}_{name}.csv"
        else:
            # If multiple SIC codes were used, save the file with a common name
            name = "Filtered_Worksheet.csv"
            filename = name
        df = pd.DataFrame(rows)
        df.to_csv(filename, index=False)
        print(f"Saved filtered data for target: {name} in {filename}")


if __name__ == "__main__":
    # The actual path to CSV file
    csv_file_path = 'BasicCompanyDataAsOneFile-2023-10-04.csv'

    process_csv(csv_file_path, main_target_numbers, chunk_size=1000)
