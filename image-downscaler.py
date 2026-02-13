import os
import argparse
from PIL import Image

# Define color codes as constants for easier use
# Used to print in color in the terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m' # Reset color


# Function to get arguments from terminal
def GetArguments():
    oParser = argparse.ArgumentParser( description = "Image Downscaler" )

    oParser.add_argument(
        "source",
        help = "Path to file or folder"
    )

    oParser.add_argument(
        "--width",
        "-wt",
        type = int,
        default = None,
        help = "Target Width for resizing"
    )

    oParser.add_argument(
        "--height",
        "-ht",
        type = int,
        default = None,
        help = "Target Height for resizing"
    )

    oParser.add_argument(
        "--output",
        "-o",
        default = "resized-by-python",
        help = "Output Folder"
    )

    oArgs = oParser.parse_args()

    return oArgs.source, oArgs.width, oArgs.height, oArgs.output


# Function to downscale image to specific dimensions
def DownscaleImage( sImagePath, sOutputFolder, iTargetWidth, iTargetHeight ):
    # Downscale images but keeps aspect ratio
    try:
        # open image from image path provided using the library/package Pillow
        with Image.open( sImagePath ) as oImage:
            iOriginalWidth, iOriginalHeight = oImage.size

            # Case 1: Only width was provided
            if iTargetWidth and not iTargetHeight:
                fRatio = iTargetWidth / float( iOriginalWidth )
                tNewSize = ( iTargetWidth, int( iOriginalHeight * fRatio ) )
            
            # Case 2: Only height was provided
            elif iTargetHeight and not iTargetWidth:
                fRatio = iTargetHeight / float( iOriginalHeight )
                tNewSize = ( int( iOriginalWidth * fRatio ), iTargetHeight )
            
            # Case 3: Both width and height provided
            elif iTargetWidth and iTargetHeight:
                fWidthRatio = iTargetWidth / float( iOriginalWidth )
                fHeightRatio = iTargetHeight / float( iOriginalHeight )
                # Use smaller ratio to ensure aspect ratio is maintained
                fRatio = min( fWidthRatio, fHeightRatio )
                tNewSize = ( int( iOriginalWidth * fRatio ), int( iOriginalHeight * fRatio ) )

            else: 
                print( f"{ Colors.YELLOW }[SKIP]{ Colors.ENDC } No dimensions provided." )
                return
            
            # Downscale image
            oResizedImage = oImage.resize( tNewSize, Image.Resampling.LANCZOS )

            # Save resized image to the output folder path
            # First check if output folder exists, if not create it
            sOutputFolder = f"{ sOutputFolder }-{ tNewSize[ 0 ] }x{ tNewSize[ 1 ] }"
            if not os.path.exists( sOutputFolder ):
                os.makedirs( sOutputFolder )

            sFilenameWithoutExt = os.path.splitext( os.path.basename( sImagePath ) )[ 0 ]
            sFilenameExtension = os.path.splitext( os.path.basename( sImagePath ) )[ 1 ]
            sFilename = f"{ sFilenameWithoutExt }-1{ sFilenameExtension }"
            sSavePath = os.path.join( sOutputFolder, sFilename )
            oResizedImage.save( sSavePath )
            print( f"{ Colors.GREEN }[SUCCESS]{  Colors.ENDC} { sSavePath } -> { tNewSize[ 0 ] }x{ tNewSize[ 1 ] }" )


    # Print error if any occured
    except Exception as e:
        print( f"{ Colors.RED }[ERROR]{ Colors.ENDC } Could not process { sImagePath }: { e }" )


# Main Logic that executes
def main():
    # Get arguments parsed via terminal input
    sSource, iWidth, iHeight, sOutput = GetArguments()

    # Error handling 
    if not sSource: 
        print( f"{ Colors.RED }[ERROR]{ Colors.ENDC } Source for resizing not specified." )
        return
    
    if not iWidth and not iHeight:
        print( f"{ Colors.RED }[ERROR]{ Colors.ENDC } You must specify at least --width/-wt or --height/-ht." )
        return
    
    # Checking if source is either a file to be processed or a whole folder
    tExtensions = ( '.jpg', '.jpeg', '.png', '.webp', '.bmp' )

    if os.path.isfile( sSource ):
        # if is a file with right extensions, process file to be downscaled
        sFilename = os.path.basename( sSource )
        if sFilename.lower().endswith( tExtensions ):
            DownscaleImage( sSource, sOutput, iWidth, iHeight )
    elif os.path.isdir( sSource ):
        # if a directory/folder, then loop through each file in it then
        for sFilename in os.listdir( sSource ):
            # if is a file with right extensions, process file to be downscaled
            if sFilename.lower().endswith( tExtensions ):
                DownscaleImage( os.path.join( sSource, sFilename ), sOutput, iWidth, iHeight )
    else:
        print( f"{ Colors.RED }[ERROR]{ Colors.ENDC } Path not found: {sSource}" )


if __name__ == "__main__":
    main()
