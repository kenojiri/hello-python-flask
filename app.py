from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World!"

#see: https://docs.cloudfoundry.org/buildpacks/python/index.html#run-web-server
if __name__ == "__main__":
  port = int(os.getenv("PORT", 8080))
  app.run(host='0.0.0.0', port=port, debug=True)
