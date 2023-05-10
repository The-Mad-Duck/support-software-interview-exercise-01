import sqlite3

from flask import Flask, render_template, request,session,flash,jsonify
import sqlite3
import os
import pandas as pd
import json


con = sqlite3.connect('batch_records', check_same_thread=False)
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


# home page
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        """
        submitted_before = request.form['submitted_before']
        submitted_after = request.form['submitted_after']
        min_nodes = request.form['min_nodes']
        max_nodes = request.form['max_nodes']
        buildQueries = ""
        if submitted_before:
            buildQueries += "submitted_at"
        df = pd.read_sql(f'''SELECT * FROM BatchRecords {'WHERE' if buildQueries != "" else ''}''')
        return render_template('result.html', rows=df)
        """
        return render_template('home.html')
    elif request.method == 'GET':
        return render_template('home.html')

@app.route('/batch_jobs', methods=['POST', 'GET'])
def result():
    url = request.url
    builder = ""
    args = request.args
    if args:
        # Grab arguments to build query
        if 'filter[submitted_before]' in args:
            builder += f"submitted_at <= {args['filter[submitted_before]']}"
        if 'filter[submitted_after]' in args:
            builder += (" AND " if builder != "" else "") + f"submitted_at >= {args['filter[submitted_after]']}"
        if 'filter[min_nodes]' in args:
            builder += (" AND " if builder != "" else "") + f"nodes_used >= {args['filter[min_nodes]']}"
        if 'filter[max_nodes]' in args:
            builder += (" AND " if builder != "" else "") + f"nodes_used <= {args['filter[max_nodes]']}"
        end_dict = {"links": {"self": url}}
        try:
            # query db from builder string
            cmd = f"SELECT * FROM BatchRecords{' WHERE ' + builder if builder != '' else ''}"
            print(cmd)
            df = pd.read_sql(cmd, con)
            for row in df.iterrows():
                print(row)
            if len(df.index) < 1:
                return json.dumps(end_dict, sort_keys=False, indent=4)
            # build data for json
            data = []
            for i, row in df.iterrows():
                data.append({"type": "batch_jobs", "id": i+1, "attributes": {"batch_number": row["batch_number"],
                    "submitted_at": row["submitted_at"], "nodes_used": row["nodes_used"]}})
            end_dict["data"] = data
            Keys = list(end_dict.keys())
            Keys.sort(reverse=True)
            end_dict = {key: end_dict[key] for key in Keys}
            return json.dumps(end_dict, sort_keys=False, indent=4)
        except Exception as e:
            print(e)
            return json.dumps(end_dict, sort_keys=False, indent=4)
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host="localhost", debug=True, use_reloader=False)