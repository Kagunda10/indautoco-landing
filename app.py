from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/<path:path>/", methods=["GET", "POST"])
def index(path):
    
    manufacturer = path.split("/")[0]

    part_number = path.split("/")[1].replace("part_number=", "")

    # print(manufacturer, part_number)

    return render_template("index.html", manufacturer=manufacturer, 
                                            part_number=part_number,
                                            scroll = "form-anchor")

if __name__ == "__main__":
    app.run()