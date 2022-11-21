from quart import render_template
from PIL.Image import Image


async def flash(status: str, msg: str, template: str) -> str:
    """Flashes a success/error message on a specified template."""
    return await render_template(f'{template}.html', flash=msg, status=status)


def crop_image(image: 'Image') -> 'Image':
    width, height = image.size
    if width == height:
        return image

    offset = int(abs(height - width) / 2)

    if width > height:
        image = image.crop([offset, 0, width - offset, height])
    else:
        image = image.crop([0, offset, width, height - offset])

    return image
