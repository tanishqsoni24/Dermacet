import React from "react";

export default function Navbar() {
  return (
    <>
    <nav className="navbar navBar navbar-expand-lg">
      <div className="container-fluid">
        <div className="d-flex">
            <a className="navbar-brand brandName" href="#">
                <img src="./plugins/DermacetLogoUpdated.png" alt="" />
            </a>
            <div className="searchMenu">
                <form action="" method="get" className="searchQueryBox d-flex">
                    <div className="inputSpace">
                        <img src="./plugins/search.png" alt="noImg" className="srchImg"/>
                        <input type="text" name="" id="" placeholder="Search Products Here"/>
                    </div>
                    <button type="submit">Search</button>
                </form>
            </div>
        </div>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav mb-lg-0 navItems">
            <li className="nav-item">
              <a className="nav-link" href="#">Home</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">About Us</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Shop</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Services</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Career</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">Contact Us</a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle userBtn" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><img src="./plugins/userAdmin.png" alt="" /></a>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="#">Login</a></li>
                    <li><a class="dropdown-item" href="#">Sign Up</a></li>
                </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    </>
  );
}