# Neatoh Hygiene Group Website

Professional commercial cleaning services website for Johannesburg.

## Files
- `index.html` — page structure and content
- `styles.css` — all styling and colors  
- `script.js` — mobile nav toggle, scroll animations, form handling
- `images/` — logo and service images
- `vercel.json` — Vercel deployment configuration
- `.gitignore` — Git ignore rules

## Local Development

Start the development server:

```bash
cd "c:\Users\CEAMORE LOGISTICS\Neatoh Clean"
python -m http.server 8000
```

Visit `http://localhost:8000` in your browser.

## Deployment Options

### Option 1: Vercel (Recommended - Easiest)

1. **Create account** at https://vercel.com
2. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```
3. **Deploy from project folder**:
   ```bash
   cd "c:\Users\CEAMORE LOGISTICS\Neatoh Clean"
   vercel --prod
   ```
4. **Connect custom domain**:
   - Dashboard → Select project → Settings → Domains
   - Add your domain (e.g., neatoh.co.za)
   - Follow DNS setup instructions from Vercel

### Option 2: GitHub + Vercel

1. **Initialize Git**:
   ```bash
   cd "c:\Users\CEAMORE LOGISTICS\Neatoh Clean"
   git init
   git config user.email "your-email@neatoh.co.za"
   git config user.name "Neatoh"
   git add .
   git commit -m "Initial commit: Neatoh website"
   ```

2. **Create GitHub repository**:
   - Go to https://github.com/new
   - Create repository named `neatoh-website`
   - Copy the code to push (e.g., `git remote add origin https://github.com/username/neatoh-website.git`)

3. **Push to GitHub**:
   ```bash
   git branch -M main
   git push -u origin main
   ```

4. **Deploy on Vercel**:
   - Go to https://vercel.com/new
   - Click "Import Git Repository"
   - Select your GitHub repository
   - Click "Deploy"

5. **Connect custom domain**:
   - Vercel Dashboard → Select project
   - Settings → Domains
   - Add your domain
   - Update DNS at your domain registrar with Vercel's nameservers

## Mobile Responsive

The site works perfectly on all devices:
- ✅ Desktop (1160px max-width)
- ✅ Tablet (responsive layout)
- ✅ Mobile (860px breakpoint, hamburger menu)

## Colors and Fonts

All colors are CSS variables in `styles.css` (`:root` section):
- Update one value and it changes everywhere
- Fonts: Archivo (headings), Inter (body) — load from Google Fonts

## Contact Form

Currently shows a thank-you message on submit. To actually receive enquiries:

1. **Option A: Formspree** (Free tier available)
   - Go to https://formspree.io
   - Create account and new form
   - Copy form endpoint (e.g., `https://formspree.io/f/abcd1234`)
   - In `index.html`, find `<form id="quoteForm">` and add: `action="your-formspree-url"`

2. **Option B: Web3Forms** (Free tier available)
   - Go to https://web3forms.com
   - Create account and get access key
   - Add to form and follow their setup

## Site Features

✅ Professional business website
✅ Responsive on all devices  
✅ Contact form with validation
✅ WhatsApp integration (+27 79 505 7107)
✅ Email contact (info@neatoh.co.za)
✅ Mobile hamburger navigation
✅ Smooth scroll animations
✅ No dependencies or build step required

## File Structure

```
Neatoh Clean/
├── index.html           # Main website
├── styles.css           # Styling
├── script.js            # JavaScript interactivity
├── vercel.json          # Vercel config
├── .gitignore           # Git ignore
├── README.md            # This file
└── images/              # Logo and images
    ├── logo.png.png
    ├── service-general.jpg
    ├── service-construction.jpg
    ├── service-rubble.jpg
    └── service-renovation.jpg
```

## Next Steps

1. ✅ Verify site works locally (http://localhost:8000)
2. ☐ Set up Vercel account (if not done)
3. ☐ Deploy to Vercel
4. ☐ Connect your domain to Vercel
5. ☐ Set up contact form backend (Formspree/Web3Forms)
6. ☐ Test on mobile devices

---

**Built with:** HTML5, CSS3, Vanilla JavaScript
**Hosted on:** Vercel
**Domain:** Your custom domain (neatoh.co.za or similar)

