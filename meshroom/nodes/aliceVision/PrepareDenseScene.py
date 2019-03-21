__version__ = "2.0"

from meshroom.core import desc


class PrepareDenseScene(desc.CommandLineNode):
    commandLine = 'aliceVision_prepareDenseScene {allParams}'
    size = desc.DynamicNodeSize('input')
    parallelization = desc.Parallelization(blockSize=40)
    commandLineRange = '--rangeStart {rangeStart} --rangeSize {rangeBlockSize}'

    inputs = [
        desc.File(
            name='input',
            label='Input',
            description='''SfMData file.''',
            value='',
            uid=[0],
        ),
        desc.ListAttribute(
            elementDesc=desc.File(
                name="imagesFolder",
                label="Images Folder",
                description="",
                value="",
                uid=[0],
            ),
            name="imagesFolders",
            label="Images Folders",
            description='Use images from specific folder(s). Filename should be the same or the image uid.',
        ),
        desc.ChoiceParam(
            name='outputFileType',
            label='Output File Type',
            description='Output file type for the undistorted images.',
            value='exr',
            values=['jpg', 'png', 'tif', 'exr'],
            exclusive=True,
            uid=[0],
            advanced=True
        ),
        desc.BoolParam(
            name='saveMetadata',
            label='Save Metadata',
            description='Save projections and intrinsics information in images metadata (only for .exr images).',
            value=True,
            uid=[0],
            advanced=True
        ),
        desc.BoolParam(
            name='saveMatricesTxtFiles',
            label='Save Matrices Text Files',
            description='Save projections and intrinsics information in text files.',
            value=False,
            uid=[0],
            advanced=True
        ),
        desc.ChoiceParam(
            name='verboseLevel',
            label='Verbose Level',
            description='''verbosity level (fatal, error, warning, info, debug, trace).''',
            value='info',
            values=['fatal', 'error', 'warning', 'info', 'debug', 'trace'],
            exclusive=True,
            uid=[],
        ),
    ]

    outputs = [
        desc.File(
            name='output',
            label='Output',
            description='''Output folder.''',
            value=desc.Node.internalFolder,
            uid=[],
        ),
        desc.File(
            name='outputUndistorted',
            label='Undistorted images',
            description='List of undistorted images.',
            value=desc.Node.internalFolder + '*.{outputFileTypeValue}',
            uid=[],
            group='',
            advanced=True
            ),
    ]
