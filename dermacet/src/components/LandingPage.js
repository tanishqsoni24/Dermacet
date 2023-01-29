import React from 'react'

export default function LandingPage() {
  return (
    <div className="landingHome">
        <div className="leftSide">
            <div className="leftContentBox">
                <span className="leftContent">New Collection</span>
                <span className="leftContent">Get The Skin</span>
                <span className="leftContent">You Want To Feel</span>
                <a href="#" className="btn leftContent">Shop Now &#8594;</a>
            </div>
        </div>
        <div className="rightSide">
            <img src="./plugins/girl.png" alt="" />
        </div>
    </div>
  )
}
