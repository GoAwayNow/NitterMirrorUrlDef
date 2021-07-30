     _   _  _    _  _____   ______   
    | \ | || |  | ||  __ \ |  ____|  
    |  \| || |  | || |  | || |__     
    | . ` || |  | || |  | ||  __|    
    | |\  || |__| || |__| || |____ _ 
    |_| \_(_)____(_)_____(_)______(_)
                                  
     Nitter URL Definition Exporter
Nitter instances aren't always the most reliable thing, and keeping track of them can be difficult. Luckily, there's a service called [Twiit](https://twiiit.com/), that keeps track of functioning, non-limited Nitter instances and redirects randomly! For Hydrus, however, this means that your client needs to recongnize every functional Nitter instance.  
That's a lot.  
Well, that's where this script comes in!

## Requirements
* Python 3+ (may work on 2.7, not tested)
* Click `pip install -U click`

## Usage
First off, import this:  
![Twiit GUGs](/content/twiit_gugs.png)  
Once that's imported, you'll probably want to edit the Twitter URL classes to redirect to the new twiit classes. I don't recommend using the Twiit GUGs, as it will negatively impact your checker timings, but they're an option.

When running the script with no parameters, help text will be displayed.

To generate URL classes and GUGs, simply pass any number of Nitter instance URLs as arguments, like so:  
`python nude.py https://nitter.example.com https://nitter.example.org`

Results will be saved to .json files stored in the directory from which the script was run.

Once imported, matching URLs still need to be manually added to the parsers. Yeah, this sucks, but hey, you didn't have to make the URL classes, right?

