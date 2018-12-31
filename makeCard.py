import os
from PIL import Image, ImageDraw, ImageFont


titleFont = ImageFont.truetype( '/System/Library/Fonts/SFNSText.ttf', 18 )
cardFont  = ImageFont.truetype( '/System/Library/Fonts/SFNSText.ttf', 12 )
fontColor = ( 255, 255, 255, 128 )

# Full Card
cardWidth  = 400
cardHeight = 800

# Title 
cardTitleWidthOffset  = 10
cardTitleHeightOffset = cardWidth / 2

# Image
cardImageWidthOffset  = 20
cardImageHeightOffset = 30

# Text
cardTextWidthOffset  = 20
cardTextHeightOffset = cardHeight * .75

def makeCard(cardName, cardImage, cardText, fileName=None): 
	

	cardName = os.path.basename(cardName)

	# Create new image and an object that allows drawing onto the image
	# Drawing is for lines and text, not for inserting images
	result    = Image.new( 'RGB', (cardWidth, cardHeight) )
	drawSpace = ImageDraw.Draw(result)

	loadedCardImage = Image.open(cardImage)
	cardImageWidth , cardImageHeight = loadedCardImage.size

	# Draw in the title
	drawSpace.multiline_text( ( cardTitleHeightOffset , cardTitleWidthOffset ), cardName, font=titleFont, fill=fontColor, align='center')

	# Put the cardImage in the result
	result.paste( im=loadedCardImage, box=( cardImageWidthOffset, cardImageHeightOffset ) )

	# Draw in the text
	drawSpace.multiline_text( ( cardTextWidthOffset , cardTextHeightOffset ), cardText, font=cardFont, fill=fontColor, align='center')


	# Save Result
	if not fileName: 
		fileName = "".join(cardName.split(" ")) + ".png"

	result.save(fileName)
	print("Saved card as : " + fileName)

	return fileName

if __name__ == '__main__':
	makeCard( "Shovel", "cardImages/shovel.png", "Its a shovel, it does a dig!", "cards/shovel.png" )


