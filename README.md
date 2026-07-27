# Mountain Hydrology Group Website

Website of the Mountain Hydrology Group, an independent research collective
working on hydrology and natural hazards in mountain regions.

Built with [Jekyll](https://jekyllrb.com/) on the
[research-group-web](https://github.com/uwsampa/research-group-web) template
(CC BY-NC 4.0), adapted to build natively on GitHub Pages (no Python or
Makefile needed).

## Editing content

| What | Where |
|---|---|
| Members | `_data/people.yml` (photos in `img/people/`, referenced by the `image:` field) |
| Publications | `_data/publications.yml` (and `bib/pubs.bib` for the BibTeX download) |
| Research themes | `_projects/*.md` (one file per card; `people:` lists keys from `people.yml`) |
| News | `_posts/YYYY-MM-DD-slug.md` with `layout: post` and `shortnews: true` |
| Front-page intro | `index.html` (the `jumbotron` block) |
| Site name, nav, roles | `_config.yml` |

Missing member photos and data to verify are tracked in `PHOTOS-NEEDED.md`.

## Local preview

```sh
gem install jekyll
jekyll serve --config _config.yml,_config_dev.yml
# open http://127.0.0.1:4000/
```

`_config_dev.yml` clears the `/mhydro` path prefix used in
production so links work at the local root.

## Publishing on GitHub Pages

Easiest: run `bash ../publish-mhydro.sh` (creates the repo, pushes, and
enables Pages). Manual steps:

1. Create a repository named `mhydro` under your GitHub
   account (github.com/geokshitij).
2. Push this folder to it (`main` branch).
3. In the repository: Settings > Pages > Source: "Deploy from a branch",
   Branch: `main`, folder `/ (root)`.
4. The site appears at https://geokshitij.github.io/mhydro/

To move to a cleaner URL later, create a GitHub organization (for example
`mountainhydrology`), push to a repo named `mountainhydrology.github.io`,
and set `base: ''` in `_config.yml`.
