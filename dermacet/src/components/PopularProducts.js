import React from 'react'

export default function PopularProducts() {
  return (
    <div>
      <h2 className="PopProd_heading">
        <span>Popular </span>
        Products
      </h2>
      <div className="all_prods">
        <div className="products">
            <img src="./plugins/pimple.jpg" alt="" className="prodImg" />
            <h3 className="prodTitle">Neem Acne Free Cream</h3>
            <div className="prodReview">
                <span>⭐4.5 | </span>
                <div className="reviewBox">
                    <img src="./plugins/verified.png" alt="" />
                    <span> 4 reviews</span>
                </div>
            </div>
            <div className="prodRate">
                <span>₹220.00 <strike>₹250.00</strike></span>
            </div>
            <div className="prodBtns">
                <a className="buyBtn">Buy Now</a>
                <a className="cartBtn">Add to cart</a>
            </div>
        </div>
        <div className="products">
            <img src="./plugins/dtan.jpg" alt="" className="prodImg" />
            <h3 className="prodTitle">Neem Acne Free Cream</h3>
            <div className="prodReview">
                <span>⭐4.5 | </span>
                <div className="reviewBox">
                    <img src="./plugins/verified.png" alt="" />
                     4 reviews
                </div>
            </div>
            <div className="prodRate">
                <span>₹220.00 <strike>₹250.00</strike></span>
            </div>
            <div className="prodBtns">
                <a className="buyBtn">Buy Now</a>
                <a className="cartBtn">Add to cart</a>
            </div>
        </div>
        <div className="products">
            <img src="./plugins/onionoil.jpg" alt="" className="prodImg" />
            <h3 className="prodTitle">Neem Acne Free Cream</h3>
            <div className="prodReview">
                <span>⭐4.5 | </span>
                <div className="reviewBox">
                    <img src="./plugins/verified.png" alt="" />
                     4 reviews
                </div>
            </div>
            <div className="prodRate">
                <span>₹220.00 <strike>₹250.00</strike></span>
            </div>
            <div className="prodBtns">
                <a className="buyBtn">Buy Now</a>
                <a className="cartBtn">Add to cart</a>
            </div>
        </div>
        <div className="products">
            <img src="./plugins/ricescrub.jpg" alt="" className="prodImg" />
            <h3 className="prodTitle">Neem Acne Free Cream</h3>
            <div className="prodReview">
                <span>⭐4.5 | </span>
                <div className="reviewBox">
                    <img src="./plugins/verified.png" alt="" />
                     4 reviews
                </div>
            </div>
            <div className="prodRate">
                <span>₹220.00 <strike>₹250.00</strike></span>
            </div>
            <div className="prodBtns">
                <a className="buyBtn">Buy Now</a>
                <a className="cartBtn">Add to cart</a>
            </div>
        </div>
      </div>
      <div className="moreBtn">
        <a href="#" className="cartBtn" >See All</a>
      </div>
    </div>
  )
}
