# Resume

A static resume site built with [Pelican](https://getpelican.com/).

## Prerequisites

- [uv](https://github.com/astral-sh/uv) - Python package installer
- [just](https://github.com/casey/just) - Command runner

### Installing Prerequisites

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install just
brew install just  # macOS
# or
cargo install just  # via Rust
```

## Available Commands

Run `just` or `just --list` to see all available commands:

```bash
just                    # List all available commands
just dev                # Run development server with autoreload
just build              # Build for production
just clean              # Clean output directory
just github             # Build and deploy to GitHub Pages
```

## Development

Start the development server with live reloading:

```bash
just dev
```

The site will be available at `http://localhost:8000` (or the port configured in your Pelican settings).

## Building

Build the production version of the site:

```bash
just build
```

The output will be in `src/output/`.

## Deployment

Deploy to GitHub Pages:

```bash
just deploy
```

This will:

1. Build the production site
2. Use `ghp-import` to commit the output to the `gh-pages` branch
3. Push the changes to GitHub

## Project Structure

```text
.
├── src/
│   ├── content/       # Markdown content files
│   ├── output/        # Generated static site (gitignored)
│   ├── pelicanconf.py # Development configuration
│   └── publishconf.py # Production configuration
├── justfile           # Task runner commands
└── README.md
```
