// Copyright 2016 Proyectos y Sistemas de Mantenimiento SL (eProsima).
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/*!
 * @file UnderlayMessage.cpp
 * This source file contains the definition of the described types in the IDL
 *file.
 *
 * This file was generated by the tool gen.
 */

#include "cyber/transport/rtps/underlay_message.h"

#include "fastcdr/Cdr.h"
#include "fastcdr/exceptions/BadParamException.h"

#ifdef _WIN32
// Remove linker warning LNK4221 on Visual Studio
namespace {
char dummy;
}
#endif

namespace apollo {
namespace cyber {
namespace transport {

UnderlayMessage::UnderlayMessage() 
{
        m_timestamp = 0;
        m_seq = 0;
}

UnderlayMessage::~UnderlayMessage() {}

UnderlayMessage::UnderlayMessage(const UnderlayMessage& x) 
{
        m_timestamp = x.m_timestamp;
        m_seq = x.m_seq;
        m_data = x.m_data;
        m_datatype = x.m_datatype;
}

UnderlayMessage::UnderlayMessage(UnderlayMessage&& x) 
{
        m_timestamp = x.m_timestamp;
        m_seq = x.m_seq;
        m_data = std::move(x.m_data);
        m_datatype = std::move(x.m_datatype);
}

UnderlayMessage& UnderlayMessage::operator=(const UnderlayMessage& x) 
{
        m_timestamp = x.m_timestamp;
        m_seq = x.m_seq;
        m_data = x.m_data;
        m_datatype = x.m_datatype;

        return *this;
}

UnderlayMessage& UnderlayMessage::operator=(UnderlayMessage&& x) 
{
        m_timestamp = x.m_timestamp;
        m_seq = x.m_seq;
        m_data = std::move(x.m_data);
        m_datatype = std::move(x.m_datatype);

        return *this;
}

size_t UnderlayMessage::getMaxCdrSerializedSize(size_t current_alignment) 
{
        size_t initial_alignment = current_alignment;

        current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);

        current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);

        current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4) + 255 + 1;

        current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4) + 255 + 1;

        return current_alignment - initial_alignment;
}

size_t UnderlayMessage::getCdrSerializedSize(const UnderlayMessage& data, size_t current_alignment) 
{
        size_t initial_alignment = current_alignment;

        current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);

        current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4);

        current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4) + data.data().size() + 1;

        current_alignment += 4 + eprosima::fastcdr::Cdr::alignment(current_alignment, 4) + data.datatype().size() + 1;

        return current_alignment - initial_alignment;
}

void UnderlayMessage::serialize(eprosima::fastcdr::Cdr& scdr) const 
{
        scdr << m_timestamp;

        scdr << m_seq;

        scdr << m_data;
        scdr << m_datatype;
}

void UnderlayMessage::deserialize(eprosima::fastcdr::Cdr& dcdr) 
{
        dcdr >> m_timestamp;
        dcdr >> m_seq;
        dcdr >> m_data;
        dcdr >> m_datatype;
}

size_t UnderlayMessage::getKeyMaxCdrSerializedSize(size_t current_alignment) 
{
        size_t current_align = current_alignment;
        return current_align;
}

bool UnderlayMessage::isKeyDefined() 
{ 
        return false; 
}

void UnderlayMessage::serializeKey(eprosima::fastcdr::Cdr& scdr) const 
{
        (void)scdr;
}

}  // namespace transport
}  // namespace cyber
}  // namespace apollo
