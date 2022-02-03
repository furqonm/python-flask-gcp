import webapp2

class warmupcode(webapp2.RequestHandler):
  """
  This class handles the warmup request. You should add any code that you
  need to execute in the `get` method, such as populating caches, and ensure
  that you return a successful HTTP response.
  """

  def get(self):

      # Your warmup logic goes here.

      # Return a successful response to indicate the logic completed.
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.write('Warmup successful')

application = webapp2.WSGIApplication(
    [
        ('/_ah/warmup', warmupcode),
        # Other handlers
        # ...
    ]
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<html><body><h1>Hello World 123!</h1></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)