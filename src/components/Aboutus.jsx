import "../styles/Home.css";
export default function Content() {
  return (
    <div>
      <section className="about-section" id="about">
        <div className="container">
          <div className="row">
            <div className="content-column col-lg-6 col-md-12 col-sm-12 order-2">
              <div className="inner-column">
                <div className="sec-title">
                  <span className="title">Welcome to AutoLex</span>
                  <h2>Bridging Education Gap</h2>
                </div>
                <div className="text">
                  At AutoLex, we are passionate about leveraging technology to
                  make education more accessible and inclusive for students
                  around the world. Our project aims to bridge the gap in
                  education by providing innovative solutions that empower
                  students to overcome language barriers and access educational
                  content with ease.
                </div>
                <div className="text">
                  Our system not only simplifies the learning process but also
                  enhances the learning experience by providing personalized
                  study resources tailored to students needs.At AutoLex, we
                  believe that every student deserves equal opportunities in
                  education, regardless of language barriers or geographical
                  location. By breaking down these barriers and fostering a
                  culture of inclusivity, we aspire to create a brighter future
                  where education is truly accessible to all.
                </div>
                <div className="btn-box">
                  <a href="#" className="theme-btn btn-style-one">
                    Join Us
                  </a>
                </div>
              </div>
            </div>

            <div className="image-column col-lg-6 col-md-12 col-sm-12">
              <div className="inner-column wow fadeInLeft">
                <figure className="image-1">
                  <a href="#" className="lightbox-image" data-fancybox="images">
                    {" "}
                    <img
                      title="AutoLex"
                      src="https://easy-peasy.ai/cdn-cgi/image/quality=80,format=auto,width=700/https://fdczvxmwwjwpwbeeqcth.supabase.co/storage/v1/object/public/images/229862c0-9b97-476b-9a83-eb0edbee4d13/8deec153-0d72-425c-af68-48696b2ab4cd.png"
                      alt=""
                    />{" "}
                  </a>
                </figure>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
