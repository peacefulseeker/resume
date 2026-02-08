# Resume site task runner using Pelican static site generator

# Variables
pelican := "uv run pelican"
basedir := justfile_directory() / "src"
inputdir := basedir / "content"
outputdir := basedir / "output"
conffile := basedir / "pelicanconf.py"
publishconf := basedir / "publishconf.py"

github_branch := "gh-pages"
github_message := "Update resume"

# List available recipes
default:
    @just --list

# Build for production
build:
    cd {{basedir}} && {{pelican}} {{inputdir}} -o {{outputdir}} -s {{publishconf}}

# Clean output directory
clean:
    rm -rf {{outputdir}}

# Run development server with autoreload
dev:
    cd {{basedir}} && {{pelican}} -l --autoreload {{inputdir}} -o {{outputdir}} -s {{conffile}}

# Build and deploy to GitHub Pages
deploy: build
    uv run ghp-import -m "{{github_message}}" -b {{github_branch}} {{outputdir}} --no-jekyll
    git push origin {{github_branch}}
