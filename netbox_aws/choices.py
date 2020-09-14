from utilities.choices import ChoiceSet


class VPCRegionChoices(ChoiceSet):

    REGION_US_EAST_2 = "US-East(Ohio)"
    REGION_US_EAST_1 = "US-East(N-Virginia)"
    REGION_US_WEST_1 = "US-West(N-California)"
    REGION_US_WEST_2 = "US-West-(Oregon)"
    REGION_AP_NORTHEAST_1 = "Asia-Pacific-(Tokyo)"
    REGION_AP_NORTHEAST_2 = "Asia-Pacific-(Seoul)"
    REGION_AP_SOUTH_1 = "Asia-Pacific-(Mumbai)"
    REGION_AP_SOUTHEAST_1 = "Asia-Pacific-(Singapore)"
    REGION_AP_SOUTHEAST_2 = "Asia-Pacific-(Sydney)"
    REGION_CA_CENTRAL_1 = "Canada-(Central)"
    REGION_EU_CENTRAL_1 = "EU-(Frankfurt)"
    REGION_EU_WEST_1 = "EU-(Ireland)"
    REGION_EU_WEST_2 = "EU-(London)"
    REGION_EU_WEST_3 = "EU-(Paris)"
    REGION_SA_EAST_1 = "South-America-(São-Paulo)"

    CHOICES = (
        (REGION_US_EAST_2, "US-East(Ohio)"),
        (REGION_US_EAST_1, "US-East(N-Virginia)"),
        (REGION_US_WEST_1, "US-West(N-California)"),
        (REGION_US_WEST_2, "US-West-(Oregon)"),
        (REGION_AP_NORTHEAST_1, "Asia-Pacific-(Tokyo)"),
        (REGION_AP_NORTHEAST_2, "Asia-Pacific-(Seoul)"),
        (REGION_AP_SOUTH_1, "Asia-Pacific-(Mumbai)"),
        (REGION_AP_SOUTHEAST_1, "Asia-Pacific-(Singapore)"),
        (REGION_AP_SOUTHEAST_2, "Asia-Pacific-(Sydney)"),
        (REGION_CA_CENTRAL_1, "Canada-(Central)"),
        (REGION_EU_CENTRAL_1, "EU-(Frankfurt)"),
        (REGION_EU_WEST_1, "EU-(Ireland)"),
        (REGION_EU_WEST_2, "EU-(London)"),
        (REGION_EU_WEST_3, "EU-(Paris)"),
        (REGION_SA_EAST_1, "South-America-(São-Paulo)"),
    )
