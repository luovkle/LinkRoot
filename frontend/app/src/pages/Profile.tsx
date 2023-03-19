


export const Profile = () => {
  return (
    <div className="flex gap-2">
      <div className="flex flex-1 w-60 flex-col justify-around bg-slate-100 h-screen">
        <div className="m-auto h-64 w-64 rounded-full ">
          <img 
            src="https://res.cloudinary.com/dfsye00dj/image/upload/v1679261032/look-confident_fzljjc.jpg" 
            alt="confident"
          />
        </div>
        <h1>Your Name</h1>
        <div>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque distinctio, iusto repudiandae ullam placeat voluptates alias laborum magnam rerum et repellendus unde asperiores ratione quas inventore earum, voluptatum sit perspiciatis.
          </p>
        </div>
      </div>
      <div className="flex flex-2">
        <div className="flex flex-col flex-1">
          <ul>
            <li className="py-24">Section</li>
            <li className="py-24">Section</li>
            <li className="py-24">Section</li>
          </ul>
        </div>
        <div className="flex-4">
          <div>
            <h1>Hola</h1>
          </div>
        </div>
      </div>
    </div>
  )
}