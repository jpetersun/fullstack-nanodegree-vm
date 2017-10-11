# "Database code" for the DB Forum.

import datetime

import psycopg2

POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  conn = psycopg2.connect("dbname=forum")
  cur = conn.cursor()
  posts = cur.execute("select * from posts")
  cur.close()
  conn.close()    
  return posts

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
# POSTS.append((content, datetime.datetime.now()))
  conn = psycopg2.connect("dbname=forum")
  cur = conn.cursor()
  cur.execute("insert into posts (content) values (%s)", (content,))
  cur.close()
  conn.close()

