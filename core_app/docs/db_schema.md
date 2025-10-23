## This is the prototype for the database design and related schemas
## This Document contains the schemas of the core_app

## shcemas/tables:

1. User:
     __tablename__ = "users"
    
    user_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    user_role: roles = Field(sa_column=sa.Column(Enum(roles), index=True, insert_default=roles("student")))
    hashed_password: str
    user_name: str = Field(max_length=100, nullable=False)
    user_register_no: str = Field(max_length=10, unique=True, nullable=False, index=True)
    user_email: EmailStr = Field(unique=True, nullable=False, index=True)
    department_id: int = Field(foreign_key="departments.department_id", nullable=False)

2. Department:
     __tablename__ = "departments"
    
    department_id: int = Field(primary_key=True)
    department_name: str = Field(nullable=False, index=True, max_length=20, unique=True)

3. course_room:
    __tablename__="course_rooms"
    
    course_room_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    course_room_code: str = Field(index=True, max_length=8)
    instructor_id: uuid.UUID = Field(foreign_key="users.user_id", nullable=False)
    is_archived: bool = Field(default=False)
    course_title: str = Field(nullable=False, max_length=50)
    course_sections: str = Field(max_length=50)
    course_code: str = Field(nullable=False, index=True, max_length=10)



4. enrolled_course:
    __tablename__ = "enrolled_courses"
    
    student_id: uuid.UUID = Field(foreign_key="students.student_id", nullable=False, primary_key=True)
    course_room_id: uuid.UUID = Field(foreign_key="course_rooms.course_room_id", nullable=False, primary_key=True)

5. study_resource:
    __tablename__ = "study_resources"
    
    resource_id: uuid.UUID = Field(primary_key=True)
    resource_name: str = Field(nullable=False, max_length=100)
    quiz_room_id: uuid.UUID = Field(foreign_key="quiz_rooms.quiz_room_id", nullable=False)
    url: str = Field(nullable=False)
    path: str = Field(max_length=200)
    type_of_resource: str = Field(max_length=100)
    size: float
    uploaded_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    

6. quiz_room:
    __tablename__ = "quiz_rooms"
    
    quiz_room_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    course_room_id: uuid.UUID = Field(foreign_key="course_rooms.course_room_id", nullable=False, index=True)
    quiz_room_name: str = Field(nullable=False, index=True)
    description: str

7. question:
    __tablename__ = "questions"
    
    question_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    mcq: Dict[str, Any] = Field(sa_column=sa.Column(JSONB))
    answer_index: int
    difficulty_level: str = Field(nullable=False)
    question_pool_tag: str = Field(nullable=False)
    question_type: str = Field(nullable=False)

    *structure of the mcq json*
    mcq: JSONB(
        "question": "...",
        "options": "...",
        "answer_index": "...",
        "explanation": "...",
        "difficulty": "...",
    ),

8. question_pool:
     __tablename__ = "question_pools"
    
    question_pool_tag: str = Field(primary_key=True, max_length=20)
    context_collection_name: str = Field(nullable=False)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    created_by: uuid.UUID = Field(foreign_key="users.user_id")
    pool_title: str

9. quiz_pool:
    __tablename__ = "quiz_pools"

    quiz_room_id: uuid.UUID = Field(foreign_key="quiz_rooms.quiz_room_id", primary_key=True)
    question_pool_tag: str = Field(foreign_key="question_pools.question_pool_tag", primary_key=True, max_length=20)


10. student_assignment:
     __tablename__ = "student_assignments"
    
    assignment_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    student_id: uuid.UUID = Field(foreign_key="users.user_id", index=True)
    quiz_room_id: uuid.UUID = Field(foreign_key="quiz_rooms.quiz_room_id", index=True)
    is_active: bool = Field(default=True)
    assigned_at: datetime.datetime = Field(nullable=False, default_factory=datetime.datetime.now)
    is_completed: bool = Field(nullable=False, default=False)
    completed_at: datetime.datetime = Field(nullable=False, default_factory=datetime.datetime.now)
    score: float = Field(default=0) 

11. student_question:
    __tablename__ = "student_questions"

    assigment_id: uuid.UUID = Field(foreign_key="student_assignments.assignment_id", primary_key=True, index=True)
    student_id: uuid.UUID = Field(foreign_key="users.user_id", primary_key=True, index=True)
    question_id: uuid.UUID = Field(foreign_key="questions.question_id", primary_key=True, index=True)
    is_answered: bool = Field(default=False)
    question_index: int

12. student_answer:
    __tablename__ = "student_answers"
    
    answer_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    student_id: uuid.UUID = Field(foreign_key="users.user_id", index=True)
    question_id: uuid.UUID = Field(foreign_key="questions.question_id", index=True)
    is_correct: bool
    answered_index: int
    answered_at: datetime.datetime = Field(nullable=False, default_factory=datetime.datetime.now)





 *chat history and chat messages will be moved to content_generation*
i. chat_history:
    __tablename__ = "chat_history"
    
    chat_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    quiz_room_id: uuid.UUID = Field(foreign_key="quiz_rooms.quiz_room_id", index=True)
    chat_title: str = Field(default="New chat", max_length=100)
    created_at: DateTime = Field(default_factory=datetime.datetime.now)
    message_id: uuid.UUID = Field(foreign_key="chat_messages.chat_message_id")

ii. chat_message:
    __tablename__ = "chat_history"
    
    message_id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    chat_id: uuid.UUID = Field(foreign_key="chat_history.chat_id", index=True)
    role: str
    content: str
    created_at: DateTime = Field(default_factory=datetime.datetime.now)
