# CFB Ratings

Install `uv`, set up your cfbd api key in your .env file and run `uv run cfb-ratings`.


## Dev Setup

To add pre-commit hooks; `uv run pre-commit install`.


## Todo

* Ultimately, Marimo notebook with deserving ratings published to github pages
* Figure out how to structure in `uv` to have the download piece be it's own package with shared schema as dependencies
  * Thinking structure will be download -> data transform -> analysis notebook
* Get the download over each year going
* Get polars to compute the ratings nicely for each season
