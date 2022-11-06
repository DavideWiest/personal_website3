import "https://flackr.github.io/scroll-timeline/dist/scroll-timeline.js";

const ScrollAnimImages = document.querySelectorAll(".scroll_anim");


ScrollAnimImages.forEach((image) => {
    const imgOffsetTop = image.offsetTop;
    const imgHeight = image.offsetHeight;

    const ScrollAnimImagesTimeline = new ScrollTimeline({
        scrollOffsets: [
            CSS.px(imgOffsetTop + imgHeight - window.innerHeight),
            CSS.px(imgOffsetTop - window.innerHeight * 0.75),
        ]
    });

    image.animate(
        {
            transform: [
                "perspective(1200px) rotateX(20deg) rotate(0deg)",
                "perspective(1200px) rotateX(0) rotate(26deg) translateY(15rem)"
            ],
            opacity: ["0.95", "1"]
        },
        {
            duration: 1,
            easing: "ease-in-out",
            timeline: ScrollAnimImagesTimeline
        }
    )
})

const ScrollAnimImages2 = document.querySelectorAll(".scroll_anim2");


ScrollAnimImages2.forEach((image) => {
    const imgOffsetTop = image.offsetTop;
    const imgHeight = image.offsetHeight;

    const ScrollAnimImagesTimeline2 = new ScrollTimeline({
        scrollOffsets: [
            CSS.px(imgOffsetTop + imgHeight - window.innerHeight),
            CSS.px(imgOffsetTop - window.innerHeight * 0.75),
        ]
    });

    image.animate(
        {
            transform: [
                "perspective(1200px) rotateX(20deg) rotate(0deg)",
                "perspective(1200px) rotateX(0) rotate(-26deg) translateY(-15rem)"
            ],
            opacity: ["0.95", "1"]
        },
        {
            duration: 1,
            easing: "ease-in-out",
            timeline: ScrollAnimImagesTimeline2
        }
    )
})


const ScrollAnimImages3 = document.querySelectorAll(".scroll_anim3");


ScrollAnimImages3.forEach((image) => {
    const imgOffsetTop = image.offsetTop;
    const imgHeight = image.offsetHeight;

    console.log(imgOffsetTop)
    console.log(imgHeight)

    const ScrollAnimImagesTimeline3 = new ScrollTimeline({
        scrollOffsets: [
            CSS.px(imgOffsetTop + imgHeight - window.innerHeight),
            CSS.px(imgOffsetTop - window.innerHeight * 0.75),
        ]
    });

    image.animate(
        {
            transform: [
                "perspective(1200px) rotateX(-35deg) translateY(4rem) scale(0.8)",
                "perspective(1200px) rotateX(0) scale(1)"
            ],
            opacity: ["0.85", "1"]
        },
        {
            duration: 1,
            easing: "ease-in",
            timeline: ScrollAnimImagesTimeline3
        }
    )
})