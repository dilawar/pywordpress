import argparse
import os 
from wordpress.wordpress import Wordpress
from blogger.blogger import Blogger
from pyblog.colored_print import printDebug

import sys
if sys.version_info < (3, 0) :
  from ConfigParser import RawConfigParser
else :
  from configparser import RawConfigParser 

def parseConfigFile(args):
    # Getting command line arguments   
    configFilePath = args.config
    cfg = RawConfigParser()
    with open(configFilePath, "r") as configFile :
        cfg.readfp(configFile)
    blogId = "blog{0}".format(args.blog)
    args.blogName = cfg.get(blogId, 'name')
    try:
        blog = cfg.get(blogId, 'url')
    except:
        blog = "No url given for blog."

    if "wordpress" in blog:
        args.server = "wordpress"
        blog = blog.replace("www.", "")
        blog = blog.replace("http://", "")
        blog = blog.replace("/xmlrpc.php", "")
        args.blogUrl = "http://%s/xmlrpc.php" % blog
    else:
        # Blogger uses blog name rather than url.
        args.server = "blogger"
    args.user = cfg.get(blogId,'user')
    args.password = cfg.get(blogId, 'password')
    return args

def main():
    parser = argparse.ArgumentParser(description="Wordpress client")
    parser.add_argument('--config', metavar="config"
        , default = os.environ['HOME'] + "/.config/pyblogrc"
        , help = "Config file containing setting. Default ~/.wordpressrc"
        )
    parser.add_argument('--blog', metavar="blog index in config file eg. 0, 1"
        , default = "0"
        , help = "Index of blog. If not given 0 is assumed"
        )
    parser.add_argument('--proxy', metavar="proxy"
        , help = "Setup proxy information.")
  
    parser.add_argument('--fetch', metavar="[all|post_name]"
        , help="Fetch a post with similar looking name. If 'recent' is given, it  \
            fetch and save recent posts. If 'all' is given then it fetches all\
            posts "
        )
    parser.add_argument('--update', metavar='blog_file'
        , help="Update a post."
        )
    parser.add_argument('--post', metavar='blog_file'
        , help="New post or page"
        )
    args = parser.parse_args()
    args = parseConfigFile(args)
    if args.server == "wordpress":
        printDebug("INFO", "Wordpress")
        wpObj = Wordpress(args)
    elif args.server == "blogger":
        printDebug("INFO", "Blogger")
        bgObj = Blogger(args)

if __name__ == "__main__":
    main()


