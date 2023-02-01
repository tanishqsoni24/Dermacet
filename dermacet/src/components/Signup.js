import React from 'react'

export default function Signup() {
  return (
    <div>
      <div className="banner">
        <div className="LboxForm">
            <img src="./plugins/signupgirl-removebg-preview.png" alt="" />
        </div>
        <div className="RboxForm">
            <div className="signupBox">
                <img src="./plugins/DermacetLogo.png" alt="" />
                <span>Welcome To Dermacet</span>
                    <form className="inputFields" action="" method="post">
                        <input type="text" placeholder='Full name' name="FullName" id="Fullname" />
                        <input type="email" placeholder='Email' name="FullName" id="Fullname" />
                        <input type="number" placeholder='Phone' name="" id="" />
                        <input type="password" placeholder='Create password' name="" id="" />
                        <input type="password" placeholder='Confirm password' />
                        <div className="formBtns">
                            <button type="submit" className='buyBtn'>Signup</button>
                            <span>&nbsp;&nbsp;or&nbsp;&nbsp;</span>
                            <img src="./plugins/googleIcon.png" alt="" />
                            <span>&nbsp;&nbsp;Signup with Google</span>
                        </div>
                    </form>

                
            </div>
        </div>
      </div>
    </div>
  )
}
