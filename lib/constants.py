DATA_URLS = {
    'cases': 'https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv',
    'deaths': 'https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv',
    'recovered': 'https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'
}

# Latest dictionary for US locatation values
US_LOCATIONS_IN_SOURCE = {
    "Alabama":                    'state',
    "Washington":                 'state',
    "New York":                   'state',
    "California":                 'state',
    "Massachusetts":              'state',
    "Georgia":                    'state',
    "Colorado":                   'state',
    "Florida":                    'state',
    "New Jersey":                 'state',
    "Oregon":                     'state',
    "Texas":                      'state',
    "Illinois":                   'state',
    "Pennsylvania":               'state',
    "Iowa":                       'state',
    "Maryland":                   'state',
    "North Carolina":             'state',
    "South Carolina":             'state',
    "Tennessee":                  'state',
    "Virginia":                   'state',
    "Arizona":                    'state',
    "Indiana":                    'state',
    "Kentucky":                   'state',
    "Nevada":                     'state',
    "New Hampshire":              'state',
    "Minnesota":                  'state',
    "Nebraska":                   'state',
    "Ohio":                       'state',
    "Rhode Island":               'state',
    "Wisconsin":                  'state',
    "Connecticut":                'state',
    "Hawaii":                     'state',
    "Oklahoma":                   'state',
    "Utah":                       'state',
    "Kansas":                     'state',
    "Louisiana":                  'state',
    "Missouri":                   'state',
    "Vermont":                    'state',
    "Alaska":                     'state',
    "Arkansas":                   'state',
    "Delaware":                   'state',
    "Idaho":                      'state',
    "Maine":                      'state',
    "Michigan":                   'state',
    "Mississippi":                'state',
    "Montana":                    'state',
    "New Mexico":                 'state',
    "North Dakota":               'state',
    "South Dakota":               'state',
    "West Virginia":              'state' ,
    "Wyoming":                    'state',
    "District of Columbia":       'other',
    "Washington, D.C.":           'other',
    "Kitsap, WA":                 'county',
    "Solano, CA":                 'county',
    "Santa Cruz, CA":             'county',
    "Napa, CA":                   'county',
    "Ventura, CA":                'county',
    "Worcester, MA":              'county',
    "Gwinnett, GA":               'county',
    "DeKalb, GA":                 'county',
    "Floyd, GA":                  'county',
    "Fayette, GA":                'county',
    "Gregg, TX":                  'county',
    "Monmouth, NJ":               'county',
    "Burlington, NJ":             'county',
    "Camden, NJ":                 'county',
    "Passaic, NJ":                'county',
    "Union, NJ":                  'county',
    "Eagle, CO":                  'county',
    "Larimer, CO":                'county',
    "Arapahoe, CO":               'county',
    "Gunnison, CO":               'county',
    "Kane, IL":                   'county',
    "Monroe, PA":                 'county',
    "Philadelphia, PA":           'county',
    "Norfolk, VA":                'county',
    "Arlington, VA":              'county',
    "Spotsylvania, VA":           'county',
    "Loudoun, VA":                'county',
    "Prince George's, MD":        'county',
    "Pottawattamie, IA":          'county',
    "Camden, NC":                 'county',
    "Pima, AZ":                   'county',
    "Noble, IN":                  'county',
    "Adams, IN":                  'county',
    "Boone, IN":                  'county',
    "Dane, WI":                   'county',
    "Pierce, WI":                 'county',
    "Cuyahoga, OH":               'county',
    "Weber, UT":                  'county',
    "Bennington County, VT":      'county',
    "Carver County, MN":          'county',
    "Charlotte County, FL":       'county',
    "Cherokee County, GA":        'county',
    "Collin County, TX":          'county',
    "Jefferson County, KY":       'county',
    "Jefferson Parish, LA":       'county',
    "Shasta County, CA":          'county',
    "Spartanburg County, SC":     'county',
    "Harrison County, KY":        'county',
    "Johnson County, IA":         'county',
    "Berkshire County, MA":       'county',
    "Davidson County, TN":        'county',
    "Douglas County, OR":         'county',
    "Fresno County, CA":          'county',
    "Harford County, MD":         'county',
    "Hendricks County, IN":       'county',
    "Hudson County, NJ":          'county',
    "Johnson County, KS":         'county',
    "Kittitas County, WA":        'county',
    "Manatee County, FL":         'county',
    "Marion County, OR":          'county',
    "Okaloosa County, FL":        'county',
    "Polk County, GA":            'county',
    "Riverside County, CA":       'county',
    "Shelby County, TN":          'county',
    "St. Louis County, MO":       'county',
    "Suffolk County, NY":         'county',
    "Ulster County, NY":          'county',
    "Volusia County, FL":         'county',
    "Fairfax County, VA":         'county',
    "Rockingham County, NH":      'county',
    "Montgomery County, PA":      'county',
    "Alameda County, CA":         'county',
    "Broward County, FL":         'county',
    "Lee County, FL":             'county',
    "Pinal County, AZ":           'county',
    "Rockland County, NY":        'county',
    "Saratoga County, NY":        'county',
    "Charleston County, SC":      'county',
    "Clark County, WA":           'county',
    "Cobb County, GA":            'county',
    "Davis County, UT":           'county',
    "El Paso County, CO":         'county',
    "Honolulu County, HI":        'county',
    "Jackson County, OR ":        'county',
    "Jefferson County, WA":       'county',
    "Kershaw County, SC":         'county',
    "Klamath County, OR":         'county',
    "Madera County, CA":          'county',
    "Pierce County, WA":          'county',
    "Tulsa County, OK":           'county',
    "Douglas County, CO":         'county',
    "Providence County, RI":      'county',
    "Chatham County, NC":         'county',
    "Delaware County, PA":        'county',
    "Douglas County, NE":         'county',
    "Fayette County, KY":         'county',
    "Marion County, IN":          'county',
    "Middlesex County, MA":       'county',
    "Nassau County, NY":          'county',
    "Ramsey County, MN":          'county',
    "Washoe County, NV":          'county',
    "Wayne County, PA":           'county',
    "Yolo County, CA":            'county',
    "Santa Clara County, CA":     'county',
    "Clark County, NV":           'county',
    "Fort Bend County, TX":       'county',
    "Grant County, WA":           'county',
    "Santa Rosa County, FL":      'county',
    "Williamson County, TN":      'county',
    "New York County, NY":        'county',
    "Montgomery County, MD":      'county',
    "Suffolk County, MA":         'county',
    "Denver County, CO":          'county',
    "Summit County, CO":          'county',
    "Bergen County, NJ":          'county',
    "Harris County, TX":          'county',
    "San Francisco County, CA":   'county',
    "Contra Costa County, CA":    'county',
    "Orange County, CA":          'county',
    "Norfolk County, MA":         'county',
    "Maricopa County, AZ":        'county',
    "Wake County, NC":            'county',
    "Westchester County, NY":     'county',
    "Grafton County, NH":         'county',
    "Hillsborough, FL":           'county',
    "Placer County, CA":          'county',
    "San Mateo, CA":              'county',
    "Sonoma County, CA":          'county',
    "Umatilla, OR":               'county',
    "Fulton County, GA":          'county',
    "Washington County, OR":      'county',
    "Snohomish County, WA":       'county',
    "Humboldt County, CA":        'county',
    "Sacramento County, CA":      'county',
    "San Diego County, CA":       'county',
    "San Benito, CA":             'county',
    "Los Angeles, CA":            'county',
    "King County, WA":            'county',
    "Cook County, IL":            'county',
    "Skagit, WA":                 'county',
    "Thurston, WA":               'county',
    "Island, WA":                 'county',
    "Whatcom, WA":                'county',
    "Marin, CA":                  'county',
    "Calaveras, CA":              'county',
    "Stanislaus, CA":             'county',
    "San Joaquin, CA":            'county',
    "Essex, MA":                  'county',
    "Charlton, GA":               'county',
    "Collier, FL":                'county',
    "Pinellas, FL":               'county',
    "Alachua, FL":                'county',
    "Nassau, FL":                 'county',
    "Pasco, FL":                  'county',
    "Dallas, TX":                 'county',
    "Tarrant, TX":                'county',
    "Montgomery, TX":             'county',
    "Middlesex, NJ":              'county',
    "Jefferson, CO":              'county',
    "Multnomah, OR":              'county',
    "Polk, OR":                   'county',
    "Deschutes, OR":              'county',
    "McHenry, IL":                'county',
    "Lake, IL":                   'county',
    "Bucks, PA":                  'county',
    "Hanover, VA":                'county',
    "Lancaster, SC":              'county',
    "Sullivan, TN":               'county',
    "Johnson, IN":                'county',
    "Howard, IN":                 'county',
    "St. Joseph, IN":             'county',
    "Knox, NE":                   'county',
    "Stark, OH":                  'county',
    "Anoka, MN":                  'county',
    "Olmsted, MN":                'county',
    "Summit, UT":                 'county',
    "Fairfield, CT":              'county',
    "Litchfield, CT":             'county',
    "Orleans, LA":                'county',
    "Pennington, SD":             'county',
    "Beadle, SD":                 'county',
    "Charles Mix, SD":            'county',
    "Davison, SD":                'county',
    "Minnehaha, SD":              'county',
    "Bon Homme, SD":              'county',
    "Socorro, NM":                'county',
    "Bernalillo, NM":             'county',
    "Oakland, MI":                'county',
    "Wayne, MI":                  'county',
    "New Castle, DE":             'county',
    "Puerto Rico":                'territory',
    "Virgin Islands, U.S.":       'territory',
    "Virgin Islands":             'territory',
    "Guam":                       'territory',
    "Diamond Princess":           'other',
    "Grand Princess":             'other',
}

CRUISE_SHIPS = [
    'Diamond Princess',
    'Grand Princess',
]

US_STATE_ABBREVS = {
    'AL': 'Alabama',          
    'AK': 'Alaska',           
    'AZ': 'Arizona',          
    'AR': 'Arkansas',         
    'CA': 'California',       
    'CO': 'Colorado',         
    'CT': 'Connecticut',      
    'DE': 'Delaware',         
    'FL': 'Florida',          
    'GA': 'Georgia',          
    'HI': 'Hawaii',           
    'ID': 'Idaho',            
    'IL': 'Illinois',         
    'IN': 'Indiana',          
    'IA': 'Iowa',             
    'KS': 'Kansas',           
    'KY': 'Kentucky',         
    'LA': 'Louisiana',        
    'ME': 'Maine',            
    'MD': 'Maryland',         
    'MA': 'Massachusetts',    
    'MI': 'Michigan',         
    'MN': 'Minnesota',        
    'MS': 'Mississippi',      
    'MO': 'Missouri',         
    'MT': 'Montana',          
    'NE': 'Nebraska',         
    'NV': 'Nevada',           
    'NH': 'New Hampshire',    
    'NJ': 'New Jersey',       
    'NM': 'New Mexico',       
    'NY': 'New York',         
    'NC': 'North Carolina',   
    'ND': 'North Dakota',     
    'OH': 'Ohio',             
    'OK': 'Oklahoma',         
    'OR': 'Oregon',           
    'PA': 'Pennsylvania',     
    'RI': 'Rhode Island',     
    'SC': 'South Carolina',   
    'SD': 'South Dakota',     
    'TN': 'Tennessee',        
    'TX': 'Texas',            
    'UT': 'Utah',             
    'VT': 'Vermont',          
    'VA': 'Virginia',         
    'WA': 'Washington',       
    'WV': 'West Virginia',    
    'WI': 'Wisconsin',        
    'WY': 'Wyoming',          
}

RENAMED_COLUMNS = {
    'Province/State': 'province_state',
    'Country/Region': 'country',
    'Lat': 'lat',
    'Long': 'long',
}

# https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population#Summary_of_population_by_region
US_POPULATION = {
    'Massachusetts':        {'population': 6892503,  'sub_region': 'new_england',        'region': 'northeast'},
    'Connecticut':          {'population': 3565287,  'sub_region': 'new_england',        'region': 'northeast'},
    'New Hampshire':        {'population': 1359711,  'sub_region': 'new_england',        'region': 'northeast'},
    'Maine':                {'population': 1344212,  'sub_region': 'new_england',        'region': 'northeast'},
    'Rhode Island':         {'population': 1059361,  'sub_region': 'new_england',        'region': 'northeast'},
    'Vermont':              {'population': 623989,   'sub_region': 'new_england',        'region': 'northeast'},
    'New York':             {'population': 19453561, 'sub_region': 'mid_atlantic',       'region': 'northeast'},
    'Pennsylvania':         {'population': 12801989, 'sub_region': 'mid_atlantic',       'region': 'northeast'},
    'New Jersey':           {'population': 8882190,  'sub_region': 'mid_atlantic',       'region': 'northeast'},
    'Florida':              {'population': 21477737, 'sub_region': 'south_atlantic',     'region': 'south'},
    'Georgia':              {'population': 10617423, 'sub_region': 'south_atlantic',     'region': 'south'},
    'North Carolina':       {'population': 10488084, 'sub_region': 'south_atlantic',     'region': 'south'},
    'Virginia':             {'population': 8535519,  'sub_region': 'south_atlantic',     'region': 'south'},
    'Maryland':             {'population': 6045680,  'sub_region': 'south_atlantic',     'region': 'south'},
    'South Carolina':       {'population': 5148714,  'sub_region': 'south_atlantic',     'region': 'south'},
    'West Virginia':        {'population': 1792147,  'sub_region': 'south_atlantic',     'region': 'south'},
    'Delaware':             {'population': 973764,   'sub_region': 'south_atlantic',     'region': 'south'},
    'District of Columbia': {'population': 705749,   'sub_region': 'south_atlantic',     'region': 'south'},
    'Tennessee':            {'population': 6346105,  'sub_region': 'east_south_central', 'region': 'south'},
    'Alabama':              {'population': 4903185,  'sub_region': 'east_south_central', 'region': 'south'},
    'Kentucky':             {'population': 4467673,  'sub_region': 'east_south_central', 'region': 'south'},
    'Mississippi':          {'population': 2976149,  'sub_region': 'east_south_central', 'region': 'south'},
    'Texas':                {'population': 28995881, 'sub_region': 'west_south_central', 'region': 'south'},
    'Louisiana':            {'population': 4648794,  'sub_region': 'west_south_central', 'region': 'south'},
    'Oklahoma':             {'population': 3956971,  'sub_region': 'west_south_central', 'region': 'south'},
    'Arkansas':             {'population': 3017804,  'sub_region': 'west_south_central', 'region': 'south'},
    'Illinois':             {'population': 12671821, 'sub_region': 'east_north_central', 'region': 'midwest'},
    'Ohio':                 {'population': 11689100, 'sub_region': 'east_north_central', 'region': 'midwest'},
    'Michigan':             {'population': 9986857,  'sub_region': 'east_north_central', 'region': 'midwest'},
    'Indiana':              {'population': 6732219,  'sub_region': 'east_north_central', 'region': 'midwest'},
    'Wisconsin':            {'population': 5822434,  'sub_region': 'east_north_central', 'region': 'midwest'},
    'Missouri':             {'population': 6137428,  'sub_region': 'west_north_central', 'region': 'midwest'},
    'Minnesota':            {'population': 5639632,  'sub_region': 'west_north_central', 'region': 'midwest'},
    'Iowa':                 {'population': 3155070,  'sub_region': 'west_north_central', 'region': 'midwest'},
    'Kansas':               {'population': 2913314,  'sub_region': 'west_north_central', 'region': 'midwest'},
    'Nebraska':             {'population': 1934408,  'sub_region': 'west_north_central', 'region': 'midwest'},
    'South Dakota':         {'population': 884659,   'sub_region': 'west_north_central', 'region': 'midwest'},
    'North Dakota':         {'population': 762062,   'sub_region': 'west_north_central', 'region': 'midwest'},
    'Arizona':              {'population': 7278717,  'sub_region': 'mountain',           'region': 'west'},
    'Colorado':             {'population': 5758736,  'sub_region': 'mountain',           'region': 'west'},
    'Utah':                 {'population': 3205958,  'sub_region': 'mountain',           'region': 'west'},
    'Nevada':               {'population': 3080156,  'sub_region': 'mountain',           'region': 'west'},
    'New Mexico':           {'population': 2096829,  'sub_region': 'mountain',           'region': 'west'},
    'Idaho':                {'population': 1787065,  'sub_region': 'mountain',           'region': 'west'},
    'Montana':              {'population': 1068778,  'sub_region': 'mountain',           'region': 'west'},
    'Wyoming':              {'population': 578759,   'sub_region': 'mountain',           'region': 'west'},
    'California':           {'population': 39512223, 'sub_region': 'pacific',            'region': 'west'},
    'Washington':           {'population': 7614893,  'sub_region': 'pacific',            'region': 'west'},
    'Oregon':               {'population': 4217737,  'sub_region': 'pacific',            'region': 'west'},
    'Hawaii':               {'population': 1415872,  'sub_region': 'pacific',            'region': 'west'},
    'Alaska':               {'population': 731545,   'sub_region': 'pacific',            'region': 'west'}
}
