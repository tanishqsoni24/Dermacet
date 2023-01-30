import React from 'react'

export default function ServiceLvl() {
  return (
    <div className="ServiceLvl">
        <h2 className="headMessage"><span>Unleash </span>your inner beauty with our wide range of cosmetics.</h2>
        <div className="FourCards">
            <div className="serviceCards">
                <img src="./plugins/warehouse.png" alt="" />
                <h2>Warehouse</h2>
                <h3 className="ServiceStatement">
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ipsum, atque.
                </h3>
            </div>
            <div className="serviceCards">
                <img src="./plugins/delivery.png" alt="" />
                <h2>Product Shipping</h2>
                <h3 className="ServiceStatement">
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ipsum, atque.
                </h3>
            </div>
            <div className="serviceCards">
                <img src="./plugins/customer.png" alt="" />
                <h2>Customer Support</h2>
                <h3 className="ServiceStatement">
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ipsum, atque.
                </h3>
            </div>
            <div className="serviceCards">
                <img src="./plugins/natural.png" alt="" />
                <h2>Natural Products</h2>
                <h3 className="ServiceStatement">
                    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ipsum, atque.
                </h3>
            </div>
        </div>
    </div>
  )
}
