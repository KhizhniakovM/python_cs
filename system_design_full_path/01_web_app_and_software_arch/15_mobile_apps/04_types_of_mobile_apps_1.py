# Types of Mobile Apps – Part 1
# In this lesson, I'll talk about the two different types of mobile apps: native and hybrid.

# For the record, when I say mobile apps, I specifically mean the apps that we download from the app stores like the Google Play Store and install on our mobile.

# There are two types of mobile apps: native and hybrid. In this lesson, we’ll find out what they are and what technologies are required to build these apps. In the subsequent lessons, we’ll also discuss things like:

# Why is it so important for developers to pick the right type of app, native or hybrid, to implement their use case?
# Why do we need different types of mobile apps? What are the pain points these app types are trying to solve?
# Which app type, hybrid or native, will suit best for my use case?
# So, without further ado. Let’s get on with it.

# Native app
# Native apps are apps that are built exclusively for a certain operating system
# it can be Android, iOS or Windows-based handheld device OS.

# These apps function only on the OS they are built for. For instance, an app built for Android OS will not work on Apple OS.

# Native apps interact directly with the operating system and the device hardware as opposed to communicating with it via a wrapper, an adapter or a middle layer. Therefore, they have full access to the device hardware like camera, sensors, and so on.

# These apps provide high performance, have a consistent user interface, providing the look and feel of the native OS.

# system_design_full_path/images/080.png

# Native apps don’t face any lag issues when rendering UI animations like the slider movement, hiding and displaying UI elements, etc. With these apps, the UI is pretty responsive. This means that when the user clicks on the UI, they can immediately see the change as opposed to seeing it after a bit of a lag.

# Native apps are developed using the APIs and the SDKs provided by the native OS. Some examples of native apps are the Android apps of LinkedIn, Tinder, and Hike.

# Technologies for writing Native Apps
# Every mobile OS supports a certain set of technologies for writing an app that would run on that particular OS. For instance, if you want to build an app that would run on Android OS, you can use Java, Kotlin or C++.

# Likewise, for writing native apps for iOS, you can use Swift and Objective C along with the Cocoa Touch framework.

# Similarly, every respective mobile OS supports a distinct set of technologies to enable developers to build apps for its platform.

# Hybrid app
# As the name implies, hybrid apps are a hybrid between the native and the web-based technologies. Like native apps, they can be installed from the app stores on the mobile, can access the hardware of the device, and can also communicate with the device’s OS.

# Hybrid apps are primarily built using open web-based technologies such as Html5, CSS, and JavaScript. They run in a native container and communicate with the native OS via a wrapper or a middle layer. This middle layer enables open web technologies to talk to the native OS.

# Now, because of this additional middle layer, which native apps don’t have, hybrid apps are a bit slower than native apps in performance and rendering the UI.

# system_design_full_path/images/081.png

# There are several popular frameworks available to write hybrid apps such as React-Native, Ionic, Cordova, etc.

# Technologies for writing hybrid apps
# Below are a few popular technologies for developing hybrid mobile apps.

# React Native
# React Native is an open-source mobile application development framework, written in JavaScript, developed by Facebook. Leveraging it, we can develop applications for multiple platforms like Android, iOS, Windows, etc.

# Before releasing the framework, Facebook was already using it for its ad manager, analytics, and group app. React Native is a pretty popular framework for writing hybrid apps. In 2018, it had the highest number of contributors for any repository on GitHub.

# Some of the companies using React-Native for their mobile apps are Bloomberg, Walmart, Uber Eats, and Discord.

# Apache Cordova
# Apache Cordova is an open-source hybrid mobile application development framework released by Adobe. The framework enables the developers to build mobile apps for Android, Windows, and iOS, using Html, JavaScript, and CSS.

# Several ecosystems and frameworks are built on Cordova, like Ionic Framework, PhoneGap, etc.

# Ionic framework
# Ionic is an open-source SDK for writing hybrid mobile apps built on Apache Cordova and AngularJS. This framework is leveraged by big guns in the industry like EA, GE, Amtrack, etc., to develop their mobile apps.

# Flutter
# Flutter is an open-source hybrid mobile application SDK by Google. It can be leveraged to develop applications for platforms like Android, iOS, Windows, Mac, Linux, Google Fuchsia & the web.

# This is a good Wikipedia resource that lists out various mobile app development tools, SDKs, and platforms for developing mobile apps.

# So, these are some of the popular technologies used by the industry to write hybrid apps. We will continue discussing hybrid and native apps in the next lesson.
