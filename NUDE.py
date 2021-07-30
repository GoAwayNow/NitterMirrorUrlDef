#!/usr/bin/env python -u

# N.U.D.E. - Nitter URL Definition Exporter

import sys
import os
import re
import click

# if (sys.version_info < (3, 0)):
#     from Tkinter import Tk
# else:
#     from tkinter import Tk

# From https://github.com/CuddleBear92/Hydrus-Presets-and-Scripts/blob/b8caacf88aa7d1be8118570dcc54b15b684db019/Non-Hydrus%20tools/booru.org_gug_generator/generate%20gugs.py
def gethex():
    if (sys.version_info < (3, 0)):
        return os.urandom(32).encode('hex')
    else:
        return os.urandom(32).hex()

@click.command()
@click.option('-v', '--verbose', is_flag=True)
@click.argument('mirrors', nargs=-1)
def makestring(verbose, mirrors):
    """
    \b
    Parameters
    ----------
    verbose : Boolean
        Prints regex results and final JSON to console.
    mirrors : String
        Any number of URLs pointing to the front pages
        of Nitter instances.
    \b
    Returns
    -------
    Hydrus-ready JSON saved to .json files for easy
    import.

    """
    if not mirrors:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        return
    importstring_urlc = '[26, 1, ['
    importstring_gug = '[26, 1, ['
    importstring_ngug = '[26, 1, ['
    for m in mirrors:
        mire = re.match(r'^(https?):\/\/((?:nitter\.)?(.+?)(?:\.org|\.com|\.net|\.eu|\.fr|\.de|\.services)?)\/?$', m)
        if verbose:
            click.echo('%s' % str(mire[0]))
            click.echo('%s' % str(mire[1]))
            click.echo('%s' % str(mire[2]))
            click.echo('%s' % str(mire[3]))
            
    
        importstring_urlc += '[50, "nitter ('+str(mire[3])+' mirror) media timeline", 10, ["'+gethex()+'", 3, "'+str(mire[1])+'", "'+str(mire[2])+'", [false, false, false, true, false, false], [[[51, 1, [2, "[^pic]", null, null, "shiontaso"]], null], [[51, 1, [0, "media", null, null, "media"]], null]], [], [], [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], 0, [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], null, null, 1, "'+str(mire[0]).rstrip("/")+'/shiontaso/media"]], [50, "nitter ('+str(mire[3])+' mirror) timeline", 10, ["'+gethex()+'", 3, "'+str(mire[1])+'", "'+str(mire[2])+'", [false, false, false, true, false, false], [[[51, 1, [2, "[^pic]", null, null, "shiontaso"]], null]], [], [], [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], 0, [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], null, null, 1, "'+str(mire[0]).rstrip("/")+'/shiontaso"]], [50, "nitter ('+str(mire[3])+' mirror) tweet", 10, ["'+gethex()+'", 0, "'+str(mire[1])+'", "'+str(mire[2])+'", [false, false, true, true, false, false], [[[51, 1, [3, "", null, null, "shiontaso"]], null], [[51, 1, [0, "status", null, null, "status"]], null], [[51, 1, [1, 2, null, null, "1183016591123865600"]], null]], [], [], [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], 0, [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], null, null, 1, "'+str(mire[0]).rstrip("/")+'/shiontaso/status/1183016591123865600"]], [50, "nitter ('+str(mire[3])+' mirror) tweet media", 10, ["'+gethex()+'", 2, "'+str(mire[1])+'", "'+str(mire[2])+'", [false, false, false, true, true, false], [[[51, 1, [0, "pic", null, null, "pic"]], null], [[51, 1, [2, "media%2F.*", null, null, "media%2FEZv1zeRVcAEtBnz.jpg%3Fname%3Dorig"]], null]], [], [], [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], 0, [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], null, null, 1, "'+str(mire[0]).rstrip("/")+'/pic/media%2FEZv1zeRVcAEtBnz.jpg%3Fname%3Dorig"]], [50, "nitter ('+str(mire[3])+' mirror) tweet video", 10, ["'+gethex()+'", 2, "'+str(mire[1])+'", "'+str(mire[2])+'", [false, false, true, false, true, false], [[[51, 1, [0, "pic", null, null, "pic"]], null], [[51, 1, [2, "^video.twimg.com%2Ftweet_video%2F.+", null, null, "video.twimg.com%2Ftweet_video%2FEmtfM-0UUAEPa6D.mp4"]], null]], [], [], [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], 1, [55, 1, [[], "https://hostname.com/post/page.php?id=123456&s=view"]], null, null, 1, "'+str(mire[0]).rstrip("/")+'/pic/video.twimg.com%2Ftweet_video%2FEmtfM-0UUAEPa6D.mp4"]], '
        # GUGs, because using a variable GUG was a bad idea from the start.
        mediahex = gethex()
        retweethex = gethex()
        importstring_gug += '[69, "nitter ('+str(mire[3])+' mirror) media lookup", 1, ["'+mediahex+'", "'+str(mire[0]).rstrip("/")+'/%username%/media", "%username%", "", "twitter username", "shiontaso"]], [69, "nitter ('+str(mire[3])+' mirror) retweets lookup", 1, ["'+retweethex+'", "'+str(mire[0]).rstrip("/")+'/%username%", "%username%", "", "twitter username", "shiontaso"]], '
        # nGUGs, because get everything
        importstring_ngug += '[70, "nitter ('+str(mire[3])+' mirror) media and retweets lookup", 1, ["'+gethex()+'", "twitter username", [["'+mediahex+'", "nitter ('+str(mire[3])+' mirror) media lookup"], ["'+retweethex+'", "nitter ('+str(mire[3])+' mirror) retweets lookup"]]]], '
    
    importstring_urlc = importstring_urlc[:-2]+']]'
    importstring_gug = importstring_gug[:-2]+']]'
    importstring_ngug = importstring_ngug[:-2]+']]'
    
    # if file_output:
    #     output_file = open('.\import_me.json','w')
    #     output_file.write(importstring)
    #     output_file.close()
    #     click.echo('URL classes are now in import_me.json.')
    #     if export_gugs:
    #         click.echo('In Hydrus, go to gallery url generators->import->from json files.')
    #     else:
    #         click.echo('In Hydrus, go to url classes->import->from json files.')
    # else:
    #     Tk().clipboard_clear()
    #     Tk().clipboard_append(importstring)
    #     Tk().update()
    #     click.echo('URL classes are now on your clipboard.')
    #     if export_gugs:
    #         click.echo('In Hydrus, go to gallery url generators->import->from clipboard.')
    #     else:
    #         click.echo('In Hydrus, go to url classes->import->from clipboard.')
    
    output_file_urlc = open('.\import_url_classes.json','w')
    output_file_urlc.write(importstring_urlc)
    output_file_urlc.close()
    
    output_file_gug = open('.\import_gugs.json','w')
    output_file_gug.write(importstring_gug)
    output_file_gug.close()
    
    output_file_ngug = open('.\import_nested_gugs.json','w')
    output_file_ngug.write(importstring_ngug)
    output_file_ngug.close()
    
    click.echo('URL classes are now in .json files.\n'
               'In Hydrus, import the files as follows:\n'
               'manage gallery url generators->gallery url generators->import->from json files->import_gugs.json\n'
               'manage gallery url generators->nested gallery url generators->import->from json files->import_nested_gugs.json\n'
               'manage url classes->import->from json files->import_url_classes.json')

    click.echo('Remember, URLs still need to be added to the parsers manually.')
    if verbose:
        click.echo('%s' % importstring_urlc)
        click.echo('%s' % importstring_gug)
        click.echo('%s' % importstring_ngug)
    
if __name__ == '__main__':
    makestring()

