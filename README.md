# crawpy
An attempt at a python web crawler

### Usage

Create a mysql table. If you don't know how to do this I recommend using phpmyadmin. Collation should be `utf8_general_ci`.

Customize `settings.py` with your database *settings*.

Now you can add links to the `link` table directly or you can edit the `SEED_LINKS` list in `settings.py` and run `python explorer.py --seed`

If you're in a hurry you can leave `SEED_LINKS` alone and just seed from the command line with `python explorer.py -seed http://myfirstseed.com http://mysecondseed.net ...`

The seeding procedure is only required if you have no uncrawled links in your database (ie: first time running the crawler).

After getting a few pages, start a `harvester.py`.
You can run as many explorers and harvesters concurrently as you like.

### How it works
Each explorer gets uncrawled links from the `link` table, retrieves their html contents and dumps them into the `webpage` table.
The harvester gets an unharvested html content from the `webpage` table, extracts links, and stores them in as uncrawled links in the `link` table.

![workflow](http://i.imgur.com/QV05o.jpg)

### Todo

* Automate explorer/harvester relation
* Better error handling
