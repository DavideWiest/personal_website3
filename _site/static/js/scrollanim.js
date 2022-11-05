import "https://flackr.github.io/scroll-timeline/dist/scroll-timeline.js";

const ScrollAnimImages = document.querySelectorAll(".image_anim_on_scroll_0");


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

const ScrollAnimImages2 = document.querySelectorAll(".image_anim_on_scroll_1");


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


const ScrollAnimImages3 = document.querySelectorAll(".base_fade_in");


ScrollAnimImages3.forEach((image) => {
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