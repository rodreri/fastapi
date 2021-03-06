
from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import List
from database import SessionLocal
import models

app = FastAPI()

# ------------------------------- Herramientas CRUD ------------------------------------------------------
class Tool(BaseModel):
    id:int
    title:str
    description:str
    image:str
    link:str

    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/tools',response_model=List[Tool],
        status_code=status.HTTP_200_OK)
def get_all_tools():
    tools = db.query(models.Tool).all()
    return tools

@app.get('/tool/{tool_id}', response_model=Tool,
        status_code=status.HTTP_200_OK)
def get_an_tool(tool_id:int):
    tool = db.query(models.Tool).filter(models.Tool.id == tool_id).first()
    return tool

@app.post('/tools',response_model=Tool,
        status_code=status.HTTP_201_CREATED)
def create_an_tool(tool:Tool):

    db_item = db.query(models.Tool).filter(models.Tool.title == tool.title).first()

    if db_item is not None:
        raise HTTPException(status_code=400, details="Tool already exists")

    new_tool = models.Tool(
            title=tool.title,
            description = tool.description,
            image = tool.image,
            link = tool.link
            )

    db.add(new_tool)
    db.commit()

    return new_tool

@app.put('/tool/{tool_id}', response_model=Tool,
        status_code=status.HTTP_200_OK)
def update_an_tool(tool_id:int,tool:Tool):
    tool_to_update = db.query(models.Tool).filter(models.Tool.id == tool_id).first()
    tool_to_update.title = tool.title
    tool_to_update.description = tool.description
    tool_to_update.image = tool.image
    tool_to_update.link = tool.link

    db.commit()

    return tool_to_update

@app.delete('/tool/{tool_id}', response_model=Tool,
        status_code=status.HTTP_200_OK)
def delete_tool(tool_id:int):
    tool_to_delete = db.query(models.Tool).filter(models.Tool.id == tool_id).first()
    db.delete(tool_to_delete)
    db.commit()

    if tool_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return tool_to_delete

# ------------------------------- Cursos CRUD ------------------------------------------------------
class Course(BaseModel):
    id:int
    title:str
    description:str
    date:str
    link:str

    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/courses',response_model=List[Course],
        status_code=status.HTTP_200_OK)
def get_all_courses():
    courses = db.query(models.Course).all()
    return courses

@app.get('/course/{course_id}', response_model=Course,
        status_code=status.HTTP_200_OK)
def get_an_course(course_id:int):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    return course

@app.post('/course',response_model=Course,
        status_code=status.HTTP_201_CREATED)
def create_an_course(course:Course):

    db_item = db.query(models.Course).filter(models.Course.title == course.title).first()

    if db_item is not None:
        raise HTTPException(status_code=400, details="Course already exists")

    new_course = models.Course(
            title=course.title,
            description = course.description,
            date = course.date,
            link = course.link
            )

    db.add(new_course)
    db.commit()

    return new_course

@app.put('/course/{course_id}', response_model=Course,
        status_code=status.HTTP_200_OK)
def update_an_course(course_id:int,course:Course):
    course_to_update = db.query(models.Course).filter(models.Course.id == course_id).first()
    course_to_update.title = course.title
    course_to_update.description = course.description
    course_to_update.date = course.date
    course_to_update.link = course.link

    db.commit()

    return course_to_update

@app.delete('/course/{course_id}', response_model=Course,
        status_code=status.HTTP_200_OK)
def delete_course(course_id:int):
    course_to_delete = db.query(models.Course).filter(models.Course.id == course_id).first()
    db.delete(course_to_delete)
    db.commit()

    if course_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return course_to_delete

# ------------------------------------- Talleres CRUD -----------------------------------------
class Taller(BaseModel):
    id:int
    title:str
    description:str
    date:str
    liga:str

    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/talleres',response_model=List[Taller],
        status_code=status.HTTP_200_OK)
def get_all_talleres():
    talleres = db.query(models.Taller).all()
    return talleres

@app.get('/taller/{taller_id}', response_model=Taller,
        status_code=status.HTTP_200_OK)
def get_an_taller(taller_id:int):
    taller = db.query(models.Taller).filter(models.Taller.id == taller_id).first()
    return taller

@app.post('/taller',response_model=Taller,
        status_code=status.HTTP_201_CREATED)
def create_an_taller(taller:Taller):

    db_item = db.query(models.Taller).filter(models.Taller.title == taller.title).first()

    if db_item is not None:
        raise HTTPException(status_code=400, details="Taller already exists")

    new_taller = models.Taller(
            title=taller.title,
            description = taller.description,
            date = taller.date,
            liga = taller.liga
            )

    db.add(new_taller)
    db.commit()

    return new_taller

@app.put('/taller/{taller_id}', response_model=Taller,
        status_code=status.HTTP_200_OK)
def update_an_taller(taller_id:int,taller:Taller):
    taller_to_update = db.query(models.Taller).filter(models.Taller.id == taller_id).first()
    taller_to_update.title = taller.title
    taller_to_update.description = taller.description
    taller_to_update.date = taller.date
    taller_to_update.liga = taller.liga

    db.commit()

    return taller_to_update

@app.delete('/taller/{taller_id}', response_model=Taller,
        status_code=status.HTTP_200_OK)
def delete_taller(taller_id:int):
    taller_to_delete = db.query(models.Taller).filter(models.Taller.id == taller_id).first()
    db.delete(taller_to_delete)
    db.commit()

    if taller_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return taller_to_delete


# -----------------------------------------Material CRUD ---------------------------------------------
class Material(BaseModel):
    id:int
    title:str
    url:str

    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/material',response_model=List[Material],
        status_code=status.HTTP_200_OK)
def get_all_materials():
    materials = db.query(models.Material).all()
    return materials

@app.get('/material/{material_id}', response_model=Material,
        status_code=status.HTTP_200_OK)
def get_a_material(material_id:int):
    material = db.query(models.Material).filter(models.Material.id == material_id).first()
    return material

@app.get('/material/name/{material_name}', response_model=Material,
        status_code=status.HTTP_200_OK)
def get_a_material_for_name(material_name:str):
    search = "%{}%".format(material_name)
    material = db.query(models.Material).filter(models.Material.title.like(search)).first()
    return material

@app.post('/materials',response_model=Material,
        status_code=status.HTTP_201_CREATED)
def create_a_material(material:Material):

    db_item = db.query(models.Material).filter(models.Material.title == material.title).first()
    if db_item is not None:
        raise HTTPException(status_code=400, details="Material already exists")

    new_material = models.Material(
            title=material.title,
            url = material.url,
            )

    db.add(new_material)
    db.commit()

    return new_material

@app.put('/material/{material_id}', response_model=Material,
        status_code=status.HTTP_200_OK)
def update_a_material(material_id:int,material:Material):
    material_to_update = db.query(models.Material).filter(models.Material.id == material_id).first()
    material_to_update.title = material.title
    material_to_update.url = material.url

    db.commit()

    return material_to_update

@app.delete('/material/{material_id}', response_model=Material,
        status_code=status.HTTP_200_OK)
def delete_material(material_id:int):
    material_to_delete = db.query(models.Material).filter(models.Material.id == material_id).first()
    db.delete(material_to_delete)
    db.commit()

    if material_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return material_to_delete

# ----------------------------------- Material Videos CRUD ------------------------------------------
class Video(BaseModel):
    id:int
    id_material:int
    title:str
    code:str

    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/video',response_model=List[Video],
        status_code=status.HTTP_200_OK)
def get_all_videos():
    videos = db.query(models.Video).all()
    return videos

@app.get('/video/{video_id}', response_model=Video,
        status_code=status.HTTP_200_OK)
def get_an_video(video_id:int):
    video = db.query(models.Video).filter(models.Video.id == video_id).first()
    return video

@app.get('/videos/{material_id}', response_model=List[Video],
        status_code=status.HTTP_200_OK)
def get_a_video_for_id_material(material_id:int):
    videos = db.query(models.Video).filter(models.Video.id_material == material_id).all()
    return videos

@app.post('/videos',response_model=Video,
        status_code=status.HTTP_201_CREATED)
def create_an_video(video:Video):

    db_item = db.query(models.Video).filter(models.Video.title == video.title).first()
    if db_item is not None:
        raise HTTPException(status_code=400, details="Video already exists")

    new_video = models.Video(
            id_material=video.id_material,
            title=video.title,
            code = video.code,
            )

    db.add(new_video)
    db.commit()

    return new_video

@app.put('/video/{video_id}', response_model=Video,
        status_code=status.HTTP_200_OK)
def update_an_video(video_id:int,video:Video):
    video_to_update = db.query(models.Video).filter(models.Video.id == video_id).first()
    video_to_update.id_material = video.id_material
    video_to_update.title = video.title
    video_to_update.code = video.code

    db.commit()

    return video_to_update

@app.delete('/video/{video_id}', response_model=Video,
        status_code=status.HTTP_200_OK)
def delete_video(video_id:int):
    video_to_delete = db.query(models.Video).filter(models.Video.id == video_id).first()
    db.delete(video_to_delete)
    db.commit()

    if video_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return video_to_delete

# ---------------------------------------- Material Manuales CRUD ----------------------------------
class Handbook(BaseModel):
    id:int
    id_material:int
    title:str
    url_handbook:str

    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/handbook',response_model=List[Handbook],
        status_code=status.HTTP_200_OK)
def get_all_handbooks():
    handbooks = db.query(models.Handbook).all()
    return handbooks

@app.get('/handbook/{handbook_id}', response_model=Handbook,
        status_code=status.HTTP_200_OK)
def get_an_handbook(handbook_id:int):
    handbook = db.query(models.Handbook).filter(models.Handbook.id == handbook_id).first()
    return handbook

@app.post('/handbooks',response_model=Handbook,
        status_code=status.HTTP_201_CREATED)
def create_an_handbook(handbook:Handbook):

    db_item = db.query(models.Handbook).filter(models.Handbook.title == handbook.title).first()
    if db_item is not None:
        raise HTTPException(status_code=400, details="Handbook already exists")

    new_handbook = models.Handbook(
            id_material=handbook.id_material,
            title=handbook.title,
            url_handbook = handbook.url_handbook,
            )

    db.add(new_handbook)
    db.commit()

    return new_handbook

@app.put('/handbook/{handbook_id}', response_model=Handbook,
        status_code=status.HTTP_200_OK)
def update_an_handbook(handbook_id:int,handbook:Handbook):
    handbook_to_update = db.query(models.Handbook).filter(models.Handbook.id == handbook_id).first()
    handbook_to_update.id_material = handbook.id_material
    handbook_to_update.title = handbook.title
    handbook_to_update.url_handbook = handbook.url_handbook

    db.commit()

    return handbook_to_update

@app.delete('/handbook/{handbook_id}', response_model=Handbook,
        status_code=status.HTTP_200_OK)
def delete_handbook(handbook_id:int):
    handbook_to_delete = db.query(models.Handbook).filter(models.Handbook.id == handbook_id).first()
    db.delete(handbook_to_delete)
    db.commit()

    if handbook_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return handbook_to_delete

# -------------------------------------- Material Temas CRUD -----------------------------------
class Topic(BaseModel):
    id:int
    id_material:int
    title:str
    url_notes:str

    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/topic',response_model=List[Topic],
        status_code=status.HTTP_200_OK)
def get_all_topics():
    topics = db.query(models.Topic).all()
    return topics

@app.get('/topic/{topic_id}', response_model=Topic,
        status_code=status.HTTP_200_OK)
def get_a_topic(topic_id:int):
    topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    return topic

@app.get('/topics/{material_id}', response_model=List[Topic],
        status_code=status.HTTP_200_OK)
def get_a_topic_for_id_material(material_id:int):
    topics = db.query(models.Topic).filter(models.Topic.id_material == material_id).all()
    return topics

@app.post('/topics',response_model=Topic,
        status_code=status.HTTP_201_CREATED)
def create_a_topic(topic:Topic):

    db_item = db.query(models.Topic).filter(models.Topic.title == topic.title).first()
    if db_item is not None:
        raise HTTPException(status_code=400, details="Topic already exists")

    new_topic = models.Topic(
            id_material=topic.id_material,
            title=topic.title,
            url_notes = topic.url_notes,
            )

    db.add(new_topic)
    db.commit()

    return new_topic

@app.put('/topic/{topic_id}', response_model=Topic,
        status_code=status.HTTP_200_OK)
def update_an_topic(topic_id:int,topic:Topic):
    topic_to_update = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    topic_to_update.id_material = topic.id_material
    topic_to_update.title = topic.title
    topic_to_update.url_notes = topic.url_notes

    db.commit()

    return topic_to_update

@app.delete('/topic/{topic_id}', response_model=Topic,
        status_code=status.HTTP_200_OK)
def delete_topic(topic_id:int):
    topic_to_delete = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    db.delete(topic_to_delete)
    db.commit()

    if topic_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return topic_to_delete

# -------------------------------------- Feedback CRUD ------------------------------------------
class Feedbaack(BaseModel):
    id:int
    score:str
    comments:str 
    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/feedback',response_model=List[Feedbaack],
        status_code=status.HTTP_200_OK)
def get_all_feedback():
    feedback = db.query(models.Feedback).all()
    return feedback

@app.post('/feedback',response_model=Feedbaack,
        status_code=status.HTTP_201_CREATED)
def create_new_feedback(fb:Feedbaack):

    db_item = db.query(models.Feedback).filter(models.Feedback.id == fb.id).first()
    if db_item is not None:
        raise HTTPException(status_code=400, details="FdBk already exists")

    new_fb = models.Feedback(
            score=fb.score,
            comments=fb.comments
            )

    db.add(new_fb)
    db.commit()

    return new_fb

@app.delete('/feedback/{feedback_id}', response_model=Feedbaack,
        status_code=status.HTTP_200_OK)
def delete_feedback(feedback_id:int):
    fb_to_delete = db.query(models.Feedback).filter(models.Feedback.id == feedback_id).first()
    db.delete(fb_to_delete)
    db.commit()

    if fb_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return fb_to_delete

# -------------------------------------- Consultancies CRUD ------------------------------------------
class Consultancies(BaseModel):
    id:int
    url_consultancies:str
    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/consultancies',response_model=List[Consultancies],
        status_code=status.HTTP_200_OK)
def get_all_consultancies():
    consultancies = db.query(models.Consultancies).all()
    return consultancies

@app.post('/consultancies',response_model=Consultancies,
        status_code=status.HTTP_201_CREATED)
def create_new_consultancies(consultancies:Consultancies):

    db_item = db.query(models.Consultancies).filter(models.Consultancies.id == consultancies.id).first()
    if db_item is not None:
        raise HTTPException(status_code=400, details="Consultancies already exists")

    new_Consultancies = models.Consultancies(
            url_consultancies=consultancies.url_consultancies
            )

    db.add(new_Consultancies)
    db.commit()

    return new_Consultancies

@app.put('/consultancies/{consultancies_id}', response_model=Consultancies,
        status_code=status.HTTP_200_OK)
def update_an_consultancie(consultancies_id:int,consultancies:Consultancies):
    consultancies_to_update = db.query(models.Consultancies).filter(models.Consultancies.id == consultancies_id).first()
    consultancies_to_update.url_consultancies = consultancies.url_consultancies

    db.commit()

    return consultancies_to_update

@app.delete('/consultancies/{consultancies_id}', response_model=Consultancies,
        status_code=status.HTTP_200_OK)
def delete_consultancies(consultancies_id:int):
    consultancies_to_delete = db.query(models.Consultancies).filter(models.Consultancies.id == consultancies_id).first()
    db.delete(consultancies_to_delete)
    db.commit()

    if consultancies_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return consultancies_to_delete

# -------------------------------------- Announcement CRUD ------------------------------------------
class Announcement(BaseModel):
    id:int
    url_announcement:str
    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/announcement',response_model=List[Announcement],
        status_code=status.HTTP_200_OK)
def get_all_announcement():
    announcement = db.query(models.Announcement).all()
    return announcement

@app.post('/announcement',response_model=Announcement,
        status_code=status.HTTP_201_CREATED)
def create_new_announcement(announcement:Announcement):

    db_item = db.query(models.Announcement).filter(models.Announcement.id == announcement.id).first()
    if db_item is not None:
        raise HTTPException(status_code=400, details="Announcement already exists")

    new_Announcement = models.Announcement(
            url_announcement=announcement.url_announcement
            )

    db.add(new_Announcement)
    db.commit()

    return new_Announcement

@app.put('/announcement/{announcement_id}', response_model=Announcement,
        status_code=status.HTTP_200_OK)
def update_an_announcement(announcement_id:int,announcement:Announcement):
    announcement_to_update = db.query(models.Announcement).filter(models.Announcement.id == announcement_id).first()
    announcement_to_update.url_announcement = announcement.url_announcement

    db.commit()

    return announcement_to_update

@app.delete('/announcement/{announcement_id}', response_model=Announcement,
        status_code=status.HTTP_200_OK)
def delete_announcement(announcement_id:int):
    announcement_to_delete = db.query(models.Announcement).filter(models.Announcement.id == announcement_id).first()
    db.delete(announcement_to_delete)
    db.commit()

    if announcement_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return announcement_to_delete