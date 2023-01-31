import React from 'react'

export default function Login() {
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
                        <input type="text" placeholder='Email/Phone' name="FullName" id="Fullname" />
                        <input type="password" placeholder='Enter password' name="" id="" />
                        <div className="formBtns">
                            <button type="submit" className='buyBtn'>Login</button>
                            <span>&nbsp;&nbsp;or&nbsp;&nbsp;</span>
                            <img src="./plugins/googleIcon.png" alt="" />
                            <span>&nbsp;&nbsp;Login with Google</span>
                        </div>
                    </form>
                <div className="SignupRoute">
                    <span>New user? <a href="#">Signup</a></span>
                </div>
                
            </div>
        </div>
      </div>
    </div>
  )
}
