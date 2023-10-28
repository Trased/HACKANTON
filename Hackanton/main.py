from AllignFile import Align
from SubtractFIle import Subtract
from Green_red import change_pixels

if __name__ == "__main__":

    vedere_fata_2015 = "2015_vedere_fata.png"
    vedere_fata_2019 = "2019_vedere_fata.png"

    vedere_spate_2015 = "2015_vedere_spate.png"
    vedere_spate_2019 = "2019_vedere_spate.png"

    image_output_fata = "OUTPUT_FATA_2TO1.png"
    image_output_spate = "OUTPUT_FATA_1TO2.png"

    image_output_subtraction_fata = "SUBTRACTION_FATA.png"
    image_output_subtraction_spate = "SUBTRACTION_SPATE.png"

    Align(vedere_fata_2015, vedere_fata_2019, image_output_fata)
    Subtract(vedere_fata_2019, image_output_fata, image_output_subtraction_fata)

    Align(vedere_spate_2015, vedere_spate_2019, image_output_spate)
    Subtract(vedere_spate_2019, image_output_spate, image_output_subtraction_spate)

    change_pixels("SUBTRACTION_FATA.png", "OUTPUT_FRONT.png")
    change_pixels("SUBTRACTION_SPATE.png", "OUTPUT_BACK.png")