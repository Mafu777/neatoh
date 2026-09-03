# 🚀 Deployment Guide - Neatoh Hygiene Group Website

Your website is ready to go live! Follow these steps:

---

## 📋 Quick Summary

✅ **Done:**
- Git repository initialized locally
- Mobile responsive design ready
- All content updated
- Vercel configuration included

**Next Steps:**
1. Deploy to Vercel
2. Connect your domain

---

## 🌐 Deploy to Vercel (Easiest Method)

### Step 1: Create Vercel Account
- Go to https://vercel.com
- Sign up (free)
- Verify email

### Step 2: Deploy with Vercel CLI

**Install Vercel CLI:**
```bash
npm install -g vercel
```

**Deploy your site:**
```bash
cd "c:\Users\CEAMORE LOGISTICS\Neatoh Clean"
vercel --prod
```

**What to do:**
- First time: Follow prompts to link Vercel account
- Project name: `neatoh` (or your preference)
- Framework: Select "Other" or "Static"
- Root directory: `.` (current)
- Build command: Leave blank or press Enter
- Output directory: `.` (current)

**Result:** You'll get a live URL like `https://neatoh.vercel.app`

### Step 3: Connect Your Domain

**If you own neatoh.co.za (or your domain):**

1. **In Vercel Dashboard:**
   - Go to https://vercel.com/dashboard
   - Select "neatoh" project
   - Click "Settings"
   - Click "Domains" (left sidebar)
   - Enter your domain: `neatoh.co.za` or `www.neatoh.co.za`

2. **Update DNS at Your Domain Registrar:**
   - Vercel will show you DNS records to add
   - Go to your domain registrar (wherever you bought neatoh.co.za)
   - Update nameservers OR add CNAME records (Vercel will tell you which)
   - Changes take 24-48 hours to propagate

**If you don't have a domain yet:**
- Buy one at: Namecheap, GoDaddy, Google Domains, or local registrar
- Then follow the DNS setup above

---

## 🐙 Alternative: GitHub + Vercel

More control, easier team collaboration:

### Step 1: Create GitHub Repository

**Push to GitHub:**
```bash
cd "c:\Users\CEAMORE LOGISTICS\Neatoh Clean"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/neatoh-website.git
git push -u origin main
```

(Replace `YOUR-USERNAME` with your GitHub username)

### Step 2: Deploy from GitHub to Vercel

1. Go to https://vercel.com/new
2. Click "Import Git Repository"
3. Connect GitHub account
4. Select `neatoh-website` repository
5. Click "Deploy"

### Step 3: Connect Domain

Same as above — add domain in Vercel Settings → Domains

---

## 📱 Mobile Testing

**Before going live, test on real devices:**

1. **Share localhost (while running local server):**
   ```bash
   # Get your IP address:
   ipconfig
   # Look for "IPv4 Address" (e.g., 192.168.1.100)
   # On phone, visit: http://192.168.1.100:8000
   ```

2. **After deploying to Vercel:**
   - Visit the Vercel URL on your phone
   - Test all buttons, forms, navigation
   - Check menu toggle on mobile

---

## ✉️ Contact Form Setup (Optional)

Right now, form submissions just show "Thank you" but don't send anywhere.

**To receive emails from the form:**

### Option A: Formspree (Recommended - Free)

1. Go to https://formspree.io
2. Sign up free
3. Create new form
4. Copy your form URL (e.g., `https://formspree.io/f/abc123xyz`)
5. Edit `index.html`:
   - Find: `<form id="quoteForm">`
   - Add: `action="https://formspree.io/f/abc123xyz" method="POST"`
   - Change `<button type="submit">` to work with form submission

### Option B: Web3Forms (Also Free)

1. Go to https://web3forms.com
2. Create account
3. Get your Access Key
4. Add to form and follow their setup guide

---

## 🎯 Deployment Checklist

- [ ] Vercel account created
- [ ] Vercel CLI installed
- [ ] Site deployed to Vercel
- [ ] Vercel URL working (vercel.app domain)
- [ ] Domain purchased (if needed)
- [ ] Domain connected to Vercel
- [ ] DNS propagated (wait 24-48 hours)
- [ ] Domain working (your-domain.co.za)
- [ ] Mobile tested
- [ ] Contact form working (if set up)
- [ ] All pages loading correctly
- [ ] Images displaying

---

## 🔍 Common Issues

**"Domain not found"**
- Wait 24-48 hours for DNS propagation
- Clear browser cache (Ctrl+F5)

**"Images not loading"**
- Check image paths in index.html
- Verify images in `/images/` folder
- Make sure logo is `logo.png.png` (double extension)

**"Site shows old version"**
- Hard refresh browser: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
- Clear browser cache
- Wait 5 minutes for CDN update

**"Can't connect Vercel to domain"**
- Make sure you own the domain
- Check DNS settings at registrar
- Vercel support: https://vercel.com/help

---

## 📞 Support

**For Vercel issues:**
- Docs: https://vercel.com/docs
- Support: https://vercel.com/support

**For domain issues:**
- Contact your domain registrar
- Verify DNS records propagated: https://dnschecker.org

**For website code:**
- Check README.md for file structure
- All CSS variables are in styles.css `:root`

---

## 🎉 You're Live!

Once domain is connected and DNS propagates, your site will be live at:
- `https://neatoh.co.za`
- `https://www.neatoh.co.za`

**Congratulations! Your Neatoh Hygiene Group website is ready to serve clients! 🚀**
