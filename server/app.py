# from flask import Flask
# from Run import get_clipped_videos

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "This is the LectureMe API"

# @app.route('/fetch_videos/<youtube_link>', methods=['GET'])
# def fetch_videos(youtube_link):
#   clipped_videos = get_clipped_videos(youtube_link)
#   return clipped_videos

from flask import Flask, jsonify
from Run import get_clipped_videos

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "This is the LectureMe API"

@app.route('/fetch_videos/<youtube_link>', methods=['GET'])
def fetch_videos(youtube_link):
    clipped_videos = get_clipped_videos(youtube_link)
    return jsonify(clipped_videos)

if __name__ == "__main__":
    app.run(debug=True)
