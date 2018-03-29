"""empty message

Revision ID: b4dd0add5f79
Revises:
Create Date: 2018-03-22 11:23:09.885006

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

from sqlalchemy.dialects import postgresql
from pytz import timezone as pytz_timezone
from babel import Locale

# revision identifiers, used by Alembic.
revision = 'b4dd0add5f79'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_import_error',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('event_data', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('source', sa.Enum('csv', 'shotgun', name='import_source_enum'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('department',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('color', sa.String(length=7), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('entity_type',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_entity_type_name'), 'entity_type', ['name'], unique=True)
    op.create_table('file_status',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('color', sa.String(length=7), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('task_type',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('short_name', sa.String(length=10), nullable=True),
    sa.Column('color', sa.String(length=7), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('for_shots', sa.Boolean(), nullable=True),
    sa.Column('shotgun_id', sa.Integer(), nullable=True),
    sa.Column('department_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'department_id', name='task_type_uc')
    )
    op.create_index(op.f('ix_task_type_shotgun_id'), 'task_type', ['shotgun_id'], unique=False)
    op.create_table('project_status',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('color', sa.String(length=7), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_project_status_name'), 'project_status', ['name'], unique=True)
    op.create_table('person',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=True),
    sa.Column('phone', sa.String(length=30), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('last_presence', sa.Date(), nullable=True),
    sa.Column('password', sa.Binary(), nullable=True),
    sa.Column('desktop_login', sa.String(length=80), nullable=True),
    sa.Column('shotgun_id', sa.Integer(), nullable=True),
    sa.Column('timezone', sqlalchemy_utils.types.timezone.TimezoneType(backend="pytz"), default=pytz_timezone("Europe/Paris"), nullable=True),
    sa.Column('locale', sqlalchemy_utils.types.locale.LocaleType(), default=Locale("en", "US"), nullable=True),
    sa.Column('data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('role', sa.String(length=30), nullable=True),
    sa.Column('has_avatar', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('shotgun_id')
    )
    op.create_table('department_link',
    sa.Column('person_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('department_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], )
    )
    op.create_table('task_status',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('short_name', sa.String(length=10), nullable=False),
    sa.Column('color', sa.String(length=7), nullable=False),
    sa.Column('is_reviewable', sa.Boolean(), nullable=True),
    sa.Column('is_done', sa.Boolean(), nullable=True),
    sa.Column('shotgun_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_status_is_done'), 'task_status', ['is_done'], unique=False)
    op.create_index(op.f('ix_task_status_short_name'), 'task_status', ['short_name'], unique=True)
    op.create_table('output_type',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('short_name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_output_type_name'), 'output_type', ['name'], unique=True)
    op.create_table('software',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('short_name', sa.String(length=20), nullable=False),
    sa.Column('file_extension', sa.String(length=20), nullable=False),
    sa.Column('secondary_extensions', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('project',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('shotgun_id', sa.Integer(), nullable=True),
    sa.Column('file_tree', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('project_status_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.ForeignKeyConstraint(['project_status_id'], ['project_status.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_project_name'), 'project', ['name'], unique=True)
    op.create_index(op.f('ix_project_project_status_id'), 'project', ['project_status_id'], unique=False)
    op.create_table('entity',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('name', sa.String(length=16), nullable=False),
    sa.Column('description', sa.String(length=600), nullable=True),
    sa.Column('shotgun_id', sa.Integer(), nullable=True),
    sa.Column('canceled', sa.Boolean(), nullable=True),
    sa.Column('project_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('entity_type_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('parent_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.ForeignKeyConstraint(['entity_type_id'], ['entity_type.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['entity.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'project_id', 'entity_type_id', 'parent_id', name='entity_uc')
    )
    op.create_index(op.f('ix_entity_entity_type_id'), 'entity', ['entity_type_id'], unique=False)
    op.create_index(op.f('ix_entity_parent_id'), 'entity', ['parent_id'], unique=False)
    op.create_index(op.f('ix_entity_project_id'), 'entity', ['project_id'], unique=False)
    op.create_table('entity_link',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('entity_in_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('entity_out_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('nb_occurences', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['entity_in_id'], ['entity.id'], ),
    sa.ForeignKeyConstraint(['entity_out_id'], ['entity.id'], ),
    sa.PrimaryKeyConstraint('id', 'entity_in_id', 'entity_out_id')
    )
    op.create_table('asset_instance',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('asset_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('entity_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('entity_type_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.ForeignKeyConstraint(['asset_id'], ['entity.id'], ),
    sa.ForeignKeyConstraint(['entity_id'], ['entity.id'], ),
    sa.ForeignKeyConstraint(['entity_type_id'], ['entity_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('asset_id', 'entity_id', 'number', name='asset_instance_uc'),
    sa.UniqueConstraint('entity_id', 'name', name='asset_instance_name_uc')
    )
    op.create_index(op.f('ix_asset_instance_asset_id'), 'asset_instance', ['asset_id'], unique=False)
    op.create_index(op.f('ix_asset_instance_entity_id'), 'asset_instance', ['entity_id'], unique=False)
    op.create_index(op.f('ix_asset_instance_entity_type_id'), 'asset_instance', ['entity_type_id'], unique=False)
    op.create_table('task',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('estimation', sa.Integer(), nullable=True),
    sa.Column('completion_rate', sa.Integer(), nullable=True),
    sa.Column('sort_order', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('due_date', sa.DateTime(), nullable=True),
    sa.Column('real_start_date', sa.DateTime(), nullable=True),
    sa.Column('shotgun_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('task_type_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('task_status_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('entity_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('assigner_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.ForeignKeyConstraint(['assigner_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['entity_id'], ['entity.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['task_status_id'], ['task_status.id'], ),
    sa.ForeignKeyConstraint(['task_type_id'], ['task_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'project_id', 'task_type_id', 'entity_id', name='task_uc')
    )
    op.create_index(op.f('ix_task_entity_id'), 'task', ['entity_id'], unique=False)
    op.create_index(op.f('ix_task_project_id'), 'task', ['project_id'], unique=False)
    op.create_table('time_spent',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('task_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('person_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['task.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('person_id', 'task_id', 'date', name='time_spent_uc')
    )
    op.create_index(op.f('ix_time_spent_person_id'), 'time_spent', ['person_id'], unique=False)
    op.create_index(op.f('ix_time_spent_task_id'), 'time_spent', ['task_id'], unique=False)
    op.create_table('working_file',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('shotgun_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('revision', sa.Integer(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('checksum', sa.Integer(), nullable=True),
    sa.Column('path', sa.String(length=400), nullable=True),
    sa.Column('task_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('entity_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('person_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('software_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.ForeignKeyConstraint(['entity_id'], ['entity.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['software_id'], ['software.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['task.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'task_id', 'entity_id', 'revision', name='working_file_uc')
    )
    op.create_index(op.f('ix_working_file_entity_id'), 'working_file', ['entity_id'], unique=False)
    op.create_index(op.f('ix_working_file_shotgun_id'), 'working_file', ['shotgun_id'], unique=False)
    op.create_index(op.f('ix_working_file_task_id'), 'working_file', ['task_id'], unique=False)
    op.create_table('assignations',
    sa.Column('task', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('person', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.ForeignKeyConstraint(['person'], ['person.id'], ),
    sa.ForeignKeyConstraint(['task'], ['task.id'], ),
    sa.PrimaryKeyConstraint('task', 'person')
    )
    op.create_table('output_file',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('shotgun_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('extension', sa.String(length=10), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('revision', sa.Integer(), nullable=False),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('checksum', sa.String(length=32), nullable=True),
    sa.Column('source', sa.String(length=40), nullable=True),
    sa.Column('path', sa.String(length=400), nullable=True),
    sa.Column('representation', sa.String(length=20), nullable=True),
    sa.Column('nb_elements', sa.Integer(), nullable=True),
    sa.Column('canceled', sa.Boolean(), nullable=False),
    sa.Column('uploaded_movie_url', sa.String(length=600), nullable=True),
    sa.Column('uploaded_movie_name', sa.String(length=150), nullable=True),
    sa.Column('file_status_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('entity_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('asset_instance_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('output_type_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('task_type_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('person_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('source_file_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.ForeignKeyConstraint(['asset_instance_id'], ['asset_instance.id'], ),
    sa.ForeignKeyConstraint(['entity_id'], ['entity.id'], ),
    sa.ForeignKeyConstraint(['file_status_id'], ['file_status.id'], ),
    sa.ForeignKeyConstraint(['output_type_id'], ['output_type.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['source_file_id'], ['working_file.id'], ),
    sa.ForeignKeyConstraint(['task_type_id'], ['task_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'entity_id', 'output_type_id', 'task_type_id', 'representation', 'revision', name='output_file_uc')
    )
    op.create_index(op.f('ix_output_file_asset_instance_id'), 'output_file', ['asset_instance_id'], unique=False)
    op.create_index(op.f('ix_output_file_output_type_id'), 'output_file', ['output_type_id'], unique=False)
    op.create_index(op.f('ix_output_file_representation'), 'output_file', ['representation'], unique=False)
    op.create_index(op.f('ix_output_file_task_type_id'), 'output_file', ['task_type_id'], unique=False)
    op.create_table('preview_file',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('revision', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('source', sa.String(length=40), nullable=True),
    sa.Column('shotgun_id', sa.Integer(), nullable=True),
    sa.Column('is_movie', sa.Boolean(), nullable=True),
    sa.Column('url', sa.String(length=600), nullable=True),
    sa.Column('uploaded_movie_url', sa.String(length=600), nullable=True),
    sa.Column('uploaded_movie_name', sa.String(length=150), nullable=True),
    sa.Column('task_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('person_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('source_file_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['source_file_id'], ['output_file.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['task.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'task_id', 'revision', name='preview_uc'),
    sa.UniqueConstraint('shotgun_id')
    )
    op.create_index(op.f('ix_preview_file_task_id'), 'preview_file', ['task_id'], unique=False)
    op.add_column('entity', sa.Column('preview_file_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True))
    op.create_foreign_key(
        'fk_main_preview', 'entity', 'preview_file', ['preview_file_id'], ['id']
    )
    op.create_table('playlist',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('shots', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('project_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'project_id', name='playlist_uc')
    )
    op.create_table('comment',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('shotgun_id', sa.Integer(), nullable=True),
    sa.Column('object_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('object_type', sa.String(length=80), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('task_status_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.Column('person_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('preview_file_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['preview_file_id'], ['preview_file.id'], ),
    sa.ForeignKeyConstraint(['task_status_id'], ['task_status.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_object_id'), 'comment', ['object_id'], unique=False)
    op.create_index(op.f('ix_comment_object_type'), 'comment', ['object_type'], unique=False)
    op.create_table('custom_action',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('url', sa.String(length=400), nullable=True),
    sa.Column('entity_type', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_working_file_task_id'), table_name='working_file')
    op.drop_index(op.f('ix_working_file_shotgun_id'), table_name='working_file')
    op.drop_index(op.f('ix_working_file_entity_id'), table_name='working_file')
    op.drop_table('working_file')
    op.drop_index(op.f('ix_time_spent_task_id'), table_name='time_spent')
    op.drop_index(op.f('ix_time_spent_person_id'), table_name='time_spent')
    op.drop_table('time_spent')
    op.drop_index(op.f('ix_task_type_shotgun_id'), table_name='task_type')
    op.drop_table('task_type')
    op.drop_index(op.f('ix_task_status_short_name'), table_name='task_status')
    op.drop_index(op.f('ix_task_status_is_done'), table_name='task_status')
    op.drop_table('task_status')
    op.drop_index(op.f('ix_task_project_id'), table_name='task')
    op.drop_index(op.f('ix_task_entity_id'), table_name='task')
    op.drop_table('task')
    op.drop_table('software')
    op.drop_index(op.f('ix_project_status_name'), table_name='project_status')
    op.drop_table('project_status')
    op.drop_index(op.f('ix_project_project_status_id'), table_name='project')
    op.drop_index(op.f('ix_project_name'), table_name='project')
    op.drop_table('project')
    op.drop_index(op.f('ix_preview_file_task_id'), table_name='preview_file')
    op.drop_table('preview_file')
    op.drop_table('playlist')
    op.drop_table('person')
    op.drop_index(op.f('ix_output_type_name'), table_name='output_type')
    op.drop_table('output_type')
    op.drop_index(op.f('ix_output_file_task_type_id'), table_name='output_file')
    op.drop_index(op.f('ix_output_file_representation'), table_name='output_file')
    op.drop_index(op.f('ix_output_file_output_type_id'), table_name='output_file')
    op.drop_index(op.f('ix_output_file_asset_instance_id'), table_name='output_file')
    op.drop_table('output_file')
    op.drop_table('file_status')
    op.drop_index(op.f('ix_entity_type_name'), table_name='entity_type')
    op.drop_table('entity_type')
    op.drop_table('entity_link')
    op.drop_index(op.f('ix_entity_project_id'), table_name='entity')
    op.drop_index(op.f('ix_entity_parent_id'), table_name='entity')
    op.drop_index(op.f('ix_entity_entity_type_id'), table_name='entity')
    op.drop_table('entity')
    op.drop_table('department_link')
    op.drop_table('department')
    op.drop_table('data_import_error')
    op.drop_table('custom_action')
    op.drop_index(op.f('ix_comment_object_type'), table_name='comment')
    op.drop_index(op.f('ix_comment_object_id'), table_name='comment')
    op.drop_table('comment')
    op.drop_table('assignations')
    op.drop_index(op.f('ix_asset_instance_entity_type_id'), table_name='asset_instance')
    op.drop_index(op.f('ix_asset_instance_entity_id'), table_name='asset_instance')
    op.drop_index(op.f('ix_asset_instance_asset_id'), table_name='asset_instance')
    op.drop_table('asset_instance')
    # ### end Alembic commands ###
