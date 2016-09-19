Post Pin on Pinterest
---------------------

Get the script:

.. code-block:: bash

    git clone https://github.com/ezag/pypin.git
    cd pypin


(or, if you don't want to use git, download it from
https://raw.githubusercontent.com/ezag/pypin/master/pypin.py)

Run from command line:

.. code-block:: bash

    python pypin.py \
            'eugenzagorodniy/test'      \  # board
            'Take a look, it is GitHub' \  # note
            'https://github.com/'       \  # link
            # image url:
            'https://assets-cdn.github.com/images/modules/open_graph/github-mark.png'

First run:

.. code-block:: none

    - Go to following URL in your browser: 

    https://api.pinterest.com/oauth/?scope=read_public%2Cwrite_public&redirect_uri=https%3A%2F%2Fdevelopers.pinterest.com%2Ftools%2Fapi-explorer%2F&response_type=token&client_id=4779055074072594921

    - Confirm permissions
    - You'll be redirected to another page - put its URL below:

    >

After you provide redirect URL, a ``.pypin-access-token`` file will be
created in working directory, and will be used for all subsequent
requests until access token expires.

Script output example is case of success:

.. code-block:: json

    {
      "data": {
        "url": "https://www.pinterest.com/pin/687643436823691338/", 
        "note": "Take a look, it is GitHub", 
        "link": "https://www.pinterest.com/r/pin/687643436823691338/4779055074072594921/3cdbba8c79c29eba41db0a63e1b7ea42ff8a705745fc44e54f86ec42ecd50874", 
        "id": "687643436823691338"
      }
    }
