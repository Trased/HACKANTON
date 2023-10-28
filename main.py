from AllignFile import Align
from SubtractFIle import Subtract
if __name__ == "__main__":
    image1 = "DICOMM-1-FATA.png"
    image2 = "DICOMM-2-FATA.png"
    image_output_fata_2TO1 = "OUTPUT_FATA_2TO1.png"
    image_output_fata_1TO2 = "OUTPUT_FATA_1TO2.png"
    image_output_subtraction_fata_2FROM1 = "SUBTRACTION_FATA_2FROM1.png"
    image_output_subtraction_fata_1FORM2 = "SUBTRACTION_FATA_1FROM2.png"
    Align(image1, image2, image_output_fata_2TO1)
    Subtract(image1, image_output_fata_2TO1, image_output_subtraction_fata_2FROM1)
    Align(image2, image1, image_output_fata_1TO2)
    Subtract(image_output_fata_1TO2, image1, image_output_subtraction_fata_1FORM2)
