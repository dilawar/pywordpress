import argparse
import os 
from wordpress.wordpress import Wordpress
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
    if not os.path.isfile(configFilePath):
        print("Config file {} does not exists".format(configFilePath))
        print("Create this file and retry...")
        sys.exit()
    with open(configFilePath, "r") as configFile :
        cfg.readfp(configFile)
    blogId = "blog{0}".format(args.blog)
    args.blogName = cfg.get(blogId, 'name')
    try:
        blog = cfg.get(blogId, 'url')
    except:
        blog = "No url given for blog."
        raise UserWarning(blog)

    args.server = "wordpress"
    blog = blog.replace("www.", "")
    blog = blog.replace("http://", "")
    blog = blog.replace("/xmlrpc.php", "")
    args.blogUrl = "http://%s/xmlrpc.php" % blog
    args.user = cfg.get(blogId,'user')
    args.password = cfg.get(blogId, 'password')
    return args

def main():
    parser = argparse.ArgumentParser(description="Wordpress client")
    parser.add_argument('--config', metavar="config"
        , default = os.environ['HOME'] + "/.config/twordpress/config"
        , help = "Config file containing settings: ~/.config/twordpress/config"
        )
    parser.add_argument('--blog', metavar="blog index in config file eg. 0, 1"
        , default = "0"
        , help = "Index of blog. If not given 0 is assumed"
        )
    parser.add_argument('--proxy', metavar="proxy"
        , help = "Setup proxy information.")
  
    parser.add_argument('--fetch', metavar="[all|post_name]"
        , help="Fetch a post with similar looking name. \
                If 'all' is given then it fetches all\
                posts "
        )
    parser.add_argument('--update', metavar='blog_file'
        , help="Update a post."
        )
    parser.add_argument('--new', metavar='blog_file'
        , help="New post or page"
        )
    parser.add_argument('--zemanta', metavar='zemanta'
            , help="Zemanta suggestion to embed in post"
            )
    args = parser.parse_args()
    args = parseConfigFile(args)
    if args.server == "wordpress":
        printDebug("INFO", "Wordpress `{}`".format(args.blogName))
        wpObj = Wordpress(args)
    else:
        printDebug("WARN", "It does not look like a wordpress: {}".format(
                args.server
                )
            )


if __name__ == "__main__":
    main()


