import argparse
import os 
from wordpress import Wordpress

def main():
    parser = argparse.ArgumentParser(description="Wordpress client")
    parser.add_argument('--config', metavar="config"
        , default = os.environ['HOME'] + "/.wordpressrc"
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
    wpObj = Wordpress()
    wpObj.run(args)

if __name__ == "__main__":
    main()

