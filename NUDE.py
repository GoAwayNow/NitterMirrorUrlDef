#!/usr/bin/env python -u

# N.U.D.E. - Nitter URL Definition Exporter

import sys
import os
import re
import click

if (sys.version_info < (3, 0)):
    from Tkinter import Tk
else:
    from tkinter import Tk

# From https://github.com/CuddleBear92/Hydrus-Presets-and-Scripts/blob/b8caacf88aa7d1be8118570dcc54b15b684db019/Non-Hydrus%20tools/booru.org_gug_generator/generate%20gugs.py
def gethex():
    if (sys.version_info < (3, 0)):
        return os.urandom(32).encode('hex')
    else:
        return os.urandom(32).hex()

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@click.option('-f', '--file-output', is_flag=True)
@click.argument('mirrors', nargs=-1)
def makestring(verbose, file_output, mirrors):
    """
    \b
    Parameters
    ----------
    verbose : Boolean
        Prints regex results and final JSON to console.
    file-output : Boolean
        Output resulting JSON to import_me.json instead
        of the clipboard.
    mirrors : String
        Any number of URLs pointing to the front pages
        of Nitter instances.
    \b
    Returns
    -------
    Hydrus-ready JSON stored to the clipboard for easy
    import.

    """
    if not mirrors:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        return
    importstring = '[26, 1, ['
    for m in mirrors:
        mire = re.match(r'^(https?):\/\/((?:nitter\.)?(.+?)(?:\.org|\.com|\.net|\.eu|\.fr|\.de|\.services)?)\/?$', m)
        if verbose:
            click.echo('%s' % str(mire[0]))
            click.echo('%s' % str(mire[1]))
            click.echo('%s' % str(mire[2]))
            click.echo('%s' % str(mire[3]))
    
        importstring += '[50, "nitter ('+str(mire[3])+' mirror) media timeline", 10, ["'+gethex()+'", 3, "'+str(mire[1])+'", "'+str(mire[2])+'", [false, false, false, true, false, false], [[[51, 1, [2, "[^pic]", null, null, "shiontaso"]], null], [[51, 1, [0, "media", null, null, "media"]], null]], [], [], [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], 0, [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], null, null, 1, "'+str(mire[0]).strip("/")+'/shiontaso/media"]], [50, "nitter ('+str(mire[3])+' mirror) timeline", 10, ["'+gethex()+'", 3, "'+str(mire[1])+'", "'+str(mire[2])+'", [false, false, false, true, false, false], [[[51, 1, [2, "[^pic]", null, null, "shiontaso"]], null]], [], [], [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], 0, [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], null, null, 1, "'+str(mire[0]).strip("/")+'/shiontaso"]], [50, "nitter ('+str(mire[3])+' mirror) tweet", 10, ["'+gethex()+'", 0, "'+str(mire[1])+'", "'+str(mire[2])+'", [false, false, true, true, false, false], [[[51, 1, [3, "", null, null, "shiontaso"]], null], [[51, 1, [0, "status", null, null, "status"]], null], [[51, 1, [1, 2, null, null, "1183016591123865600"]], null]], [], [], [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], 0, [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], null, null, 1, "'+str(mire[0]).strip("/")+'/shiontaso/status/1183016591123865600"]], [50, "nitter ('+str(mire[3])+' mirror) tweet media", 10, ["'+gethex()+'", 2, "'+str(mire[1])+'", "'+str(mire[2])+'", [false, false, false, true, true, false], [[[51, 1, [0, "pic", null, null, "pic"]], null], [[51, 1, [2, "media%2F.*", null, null, "media%2FEZv1zeRVcAEtBnz.jpg%3Fname%3Dorig"]], null]], [], [], [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], 0, [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], null, null, 1, "'+str(mire[0]).strip("/")+'/pic/media%2FEZv1zeRVcAEtBnz.jpg%3Fname%3Dorig"]], [50, "nitter ('+str(mire[3])+' mirror) tweet video", 10, ["'+gethex()+'", 2, "'+str(mire[1])+'", "'+str(mire[2])+'", [false, false, true, false, true, false], [[[51, 1, [0, "pic", null, null, "pic"]], null], [[51, 1, [2, "^video.twimg.com%2Ftweet_video%2F.+", null, null, "video.twimg.com%2Ftweet_video%2FEmtfM-0UUAEPa6D.mp4"]], null]], [], [], [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], 1, [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], null, null, 1, "'+str(mire[0]).strip("/")+'/pic/video.twimg.com%2Ftweet_video%2FEmtfM-0UUAEPa6D.mp4"]], '
    
    importstring = importstring[:-2]+']]'
    
    if file_output:
        output_file = open('.\import_me.json','w')
        output_file.write(importstring)
        output_file.close()
        click.echo('URL classes are now in import_me.json.\n'
               'In Hydrus, go to url classes->import->from json files.')
    else:
        Tk().clipboard_clear()
        Tk().clipboard_append(importstring)
        Tk().update()
        click.echo('URL classes are now on your clipboard.\n'
               'In Hydrus, go to url classes->import->from clipboard.')
    click.echo('Remember, URLs still need to be added to the parsers manually.')
    if verbose:
        click.echo('%s' % importstring)
    
if __name__ == '__main__':
    makestring()

