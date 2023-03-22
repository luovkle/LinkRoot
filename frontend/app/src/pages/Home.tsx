import { fill } from "@cloudinary/url-gen/actions/resize";
import { CloudinaryImage } from "@cloudinary/url-gen";
import { AdvancedImage } from "@cloudinary/react";

const myImage = new CloudinaryImage('sample', {cloudName: 'dfsye00dj'})
  .resize(fill().width(300).height(350));

export const Home = () => {
  return (
    <>
      <div className="
        h-screen flex">
        <div className="flex-1">
          <h1 className="text-white ">Everything you are. In one, simple link in bio</h1>
          <p className="text-white">Join 30M+ people using Linktree for their link in bio. One link to help you share everything you create, curate and sell from your Instagram, TikTok, Twitter, YouTube and other social media profiles.</p>
        </div>
        <div className="flex-1">
        </div>
      </div>
      <div className="bg-gradient-to-b from-pink-400 via-cyan-800 to-orange-500
        h-screen flex text-white">
        <div className="flex-1">Hola</div>
        <div className="flex-1">
          <div>
            <h1>Create and customize your Linktree in minutes</h1>
          </div>
          <div>
            <p>Connect your TikTok, Instagram, Twitter, website, store, videos, music, podcast, events and more. It all comes together in a link in bio landing page designed to convert.</p>
          </div>
        </div>
      </div>
    </>
  )
}