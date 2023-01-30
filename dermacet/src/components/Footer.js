import React from 'react'

export default function Footer() {
  return (
    <div className='footer'>
        <div className="footerUpbox">
            <div className="footerBoxes">
                <h2 className="linkHeadingsFooter">Product</h2>
                <div className="footerLinks">
                    <a href="">Acne Free</a>
                    <a href="">Oil</a>
                    <a href="">Career</a>
                    <a href="">Shop</a>
                    <a href="">Contact Us</a>
                </div>
            </div>
            <div className="footerBoxes">
                <h2 className="linkHeadingsFooter">Information</h2>
                <div className="footerLinks">
                    <a href="">FAQ's</a>
                    <a href="">Blog</a>
                    <a href="">Support</a>
                </div>
            </div>
            <div className="footerBoxes">
                <h2 className="linkHeadingsFooter">Company</h2>
                <div className="footerLinks">
                    <a href="">About Us</a>
                    <a href="">Career</a>
                    <a href="">Contact Us</a>
                    <a href="">Dermacet</a>
                </div>
            </div>
            <form action='' method='post' className="newsletterBox footerBoxes">
                <h3>Subscribe</h3>
                <div className="inputArea">
                    <input type="email" name="" id="" placeholder='Your Email Here!'/>
                    <button type="submit">
                        <img src="./plugins/sendArrow.png" alt="arrow" />
                    </button>
                    <p className="newsletterDescp">
                    Hello, we are Dermacet. Our goal is to develop the efficient skin care and body care products, combined institutional and home treatment to satisfy end users.
                    </p>
                </div>
            </form>
        </div>
        <div className="footerFooter">
            <img src="./plugins/DermacetLogoUpdated.png" alt="logo" className="footerLogo" />
            <div className="midLinks">
                <a href="">Terms</a>
                <a href="">Privacy</a>
                <a href="">Cookies</a>
            </div>
            <div className="footerConnections">
                <a href=""><img src="./plugins/fbicon.png" alt="fb" className="logos" /></a>
                <a href=""><img src="./plugins/instaicon.png" alt="insta" className="logos" /></a>
            </div>
        </div>
    </div>
  )
}
