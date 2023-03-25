import { fill } from "@cloudinary/url-gen/actions/resize";
import { CloudinaryImage } from "@cloudinary/url-gen";
import { AdvancedImage } from "@cloudinary/react";
import "../assets/css/Home.css";

const myImage = new CloudinaryImage('sample', {cloudName: 'dfsye00dj'})
  .resize(fill().width(300).height(350));

export const Home = () => {
  return (
    <div className="pt-20 pb-10 bg-gray-200 dark:bg-neutral-900/50 dark:text-white backdrop-blur-0 relative">
      <div className="night-background blur-2xl opacity-10 absolute top-0 -z-10 w-full h-1/5 rounded"></div>
      <div className="w-full flex justify-center mb-8">
        <div className="">
          <h1 className="font-bold text-center text-7xl mb-3">Welcome to LinkRoot</h1>
          <h2 className="text-center px-4">Link Smarter, Not Harder: With LinkRoot, The Smart Page To Manage Your Links.</h2>
          <button className="block mx-auto mt-5 bg-red-500 font-bold text-white">Get started</button>
        </div>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 m-4 rounded py-8 bg-slate-600/50 backdrop-blur-md">
        <div className="pl-8 pr-8">
          <img src="https://cdn-icons-png.flaticon.com/512/6041/6041531.png" alt="img" className="block mx-auto mb-5 max-w-full max-h-80"/>
        </div>
        <div className="pr-8 pl-8">
          <h1 className="text-right font-bold mb-2 text-4xl">Beautiful</h1>
          <h2 className="text-sm text-justify">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel fuga omnis modi, fugit facere labore. Incidunt nesciunt architecto ullam deserunt hic quam sapiente cupiditate alias, similique vero, non repellat natus?Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus optio debitis quibusdam illum molestias omnis doloremque vel porro earum quam, voluptas nostrum dolor! Perspiciatis modi quisquam culpa molestiae reiciendis asperiores!</h2>
        </div>
      </div>

      <div className="gradient-background blur-2xl opacity-20 absolute bottom-0 -z-10 w-full h-2/5 rounded"></div>
    </div>
  );
}